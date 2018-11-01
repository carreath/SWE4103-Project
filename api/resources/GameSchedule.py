from flask_restful import Resource, reqparse
from flask import request
from common import DatabaseConnector
from common import newScheduler
from common import Scheduler


class LeagueSchedule(Resource):
    def get(self):
        db_connector = DatabaseConnector()

        parser = reqparse.RequestParser()
        parser.add_argument('leagueID', type=int)
        args = parser.parse_args()

        league_id = args['leagueID']
        db_connector.cursor.execute('SELECT * FROM games WHERE leagueID = '+str(league_id))  # TODO filter out games from the past
        games = db_connector.cursor.fetchall()

        schedule_data = {}

        for game in games:
            schedule_data[game[0]] = {
                "game_id" : game[0],
                "home_team_id" : game[2],
                "away_team_id" : game[3],
                "gametime" : str(game[5]),
                "field" : game[6],
                "iscancelled" : game[7]
            }

        return schedule_data, 200

    def post(self):
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

    def update(self):
        # TODO update schedule information for a game
        return


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