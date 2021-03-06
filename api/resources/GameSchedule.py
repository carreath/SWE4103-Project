from flask_restful import Resource, reqparse, request, abort
from flask import request
from common import DatabaseConnector
from common import newScheduler
from common import Scheduler
from common import PrivilegeHandler


class LeagueSchedule(Resource):
    def get(self):
        db_connector = DatabaseConnector()

        parser = reqparse.RequestParser()
        parser.add_argument('leagueID', type=int)
        args = parser.parse_args()

        league_id = args['leagueID']
        db_connector.cursor.execute('SELECT * FROM games WHERE leagueID = '+str(league_id))
        games = db_connector.cursor.fetchall()

        schedule_data = []

        for game in games:
            schedule_data.append({
                "gameID": game[0],
                "leagueID": game[1],
                "homeTeamID": game[2],
                "awayTeamID": game[3],
                "refereeID": game[4],
                "gameTime": str(game[5]),
                "fieldName": game[6],
                "status": game[7]
            })

        return {'games': schedule_data}, 200

    def post(self):
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.game_privileges():
            abort(403, error="Unauthorized Access (invalid permissions)")

        db = DatabaseConnector()
        # 1. generate play order for teams in league
        # 2. match play order with field/time pairs given by client
        # 3. generate db data
        # EXPECTED DATA
        # {leagueID: 1,
        #  games: [ {gameTime: "2000-12-12 06:00:00", (formatted datetime str)
        #            field: "FieldA",
        #            refereeID: 1} (TODO will likely need to implement some sort of referee lookup to handle this data
        #  ]}
        data = request.get_json(force=True)
        print(data)
        leagueid = data["leagueID"]
        db.cursor.execute('SELECT * FROM teams WHERE leagueID = ' + str(leagueid))
        teams = db.cursor.fetchall()
        datelist = []
        teamlist = []
        for t in teams:
            teamlist.append(t[0])
        for g in data['games']:
            datetime = g["gameTime"]
            field = g["field"]
            ref = g['refereeID']
            datelist.append((datetime,field, ref))
        matchlist = Scheduler.create_matches(teamlist)
        print(matchlist)
        scheduleGenerator = newScheduler.findNextValid(matchlist,datelist)
        schedule = []
        for i in range(0,len(datelist)):
            schedule.append(next(scheduleGenerator))

        for s in schedule:
            homeID = s[0][0]
            awayID = s[0][1]
            gameTime = s[1][0]
            field = s[1][1]
            query = 'INSERT INTO games (leagueID, homeTeamID, awayTeamID, gameTime, field) VALUES (%d, %d, %d, \'%s\', \'%s\');' % (leagueid, homeID,awayID,gameTime,field)
            print(query)
            db.cursor.execute(query=query)

        return schedule, 200

    def put(self):
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.schedule_privileges() and not privilege_handler.update_score():
            abort(403, error="Unauthorized Access (invalid permissions)")

        parser = reqparse.RequestParser()
        parser.add_argument('gameID', type=int, required=True)
        parser.add_argument('leagueID', type=int, required=True)
        parser.add_argument('homeTeamID', type=int, required=True)
        parser.add_argument('awayTeamID', type=int, required=True)
        parser.add_argument('refereeID', type=int)
        parser.add_argument('gameTime', type=str)
        parser.add_argument('fieldName', type=str)
        parser.add_argument('status', type=str)
        args = parser.parse_args()

        game_id = args['gameID']
        league_id = args['leagueID']
        home_team_id = args['homeTeamID']
        away_team_id = args['awayTeamID']
        referee_id = args['refereeID']
        game_time = args['gameTime']
        field_name = args['fieldName']
        status = args['status']
        db = DatabaseConnector()
        db.cursor.callproc('update_game',
                            [game_id,
                             league_id,
                             home_team_id,
                             away_team_id,
                             referee_id,
                             game_time,
                             field_name,
                             status])

        db.conn.commit()
        return 200

    def delete(self):
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.schedule_privileges():
            abort(403, error="Unauthorized Access (invalid permissions)")
        parser = reqparse.RequestParser()
        parser.add_argument('leagueID', type=int, required=True)
        args = parser.parse_args()

        query = "SELECT gameID from gameMembers WHERE gameID in (SELECT gameID from games where leagueID = %s)" % args['leagueID']
        db = DatabaseConnector()
        db.cursor.execute(query)
        res = db.cursor.fetchall()
        if res:
            return 400, "Cannot delete schedule were games have been recorded"
        else:
            query = "DELETE FROM games WHERE leagueID = %s" % args['leagueID']
            db.cursor.execute(query)
            db.conn.commit()
            return 200


class PlayerSchedule(Resource):
    def get(self):
        db_connector = DatabaseConnector()
        parser = reqparse.RequestParser()
        parser.add_argument('leagueID', type=int)
        parser.add_argument('playerID', type=int)
        args = parser.parse_args()

        league_id = args['leagueID']
        player_id = args['playerID']
        db_connector.cursor.execute(
            'select * from games where leagueID = '+str(league_id)+' and (homeTeamID in (select teamID from players where playerID = '+str(player_id)+') or awayTeamID in (select teamID from players where playerID = '+str(player_id)+'));')  # TODO filter out games from the past
        games = db_connector.cursor.fetchall()

        schedule_data = {}

        for game in games:
            schedule_data[game[0]] = {
                "gameID": game[0],
                "homeTeamID": game[2],
                "awayTeamID": game[3],
                "gameTime": game[5],
                "field": game[6],
                "canceled": game[7]
            }

        return schedule_data, 200


class GameSchedule(Resource):
    def post(self):
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.schedule_privileges():
            abort(403, error="Unauthorized Access (invalid permissions)")

        parser = reqparse.RequestParser()
        parser.add_argument('leagueID', type=int, required=True)
        parser.add_argument('homeTeamID', type=int, required=True)
        parser.add_argument('awayTeamID', type=int, required=True)
        parser.add_argument('refereeID', type=int)
        parser.add_argument('gameTime', type=str)
        parser.add_argument('fieldName', type=str)
        parser.add_argument('status', type=str)
        args = parser.parse_args()

        league_id = args['leagueID']
        home_team_id = args['homeTeamID']
        away_team_id = args['awayTeamID']
        referee_id = args['refereeID']
        game_time = args['gameTime']
        field_name = args['fieldName']
        status = args['status']
        db = DatabaseConnector()
        db.cursor.callproc('create_game',
                           [league_id,
                            home_team_id,
                            away_team_id,
                            referee_id,
                            game_time,
                            field_name,
                            status])

        db.conn.commit()
        db.cursor.close()

        game_data = {
            'leagueName': league_id,
            'homeTeamID': home_team_id,
            'awayTeamID': away_team_id,
            'refereeID': referee_id,
            'gameTime': game_time,
            'fieldName': field_name,
            'status': status,
        }

        return {'game': game_data}, 201
