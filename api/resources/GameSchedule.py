from flask_restful import Resource
from flask import request
from common import DatabaseConnector


class LeagueSchedule(Resource):
    def get(self):
        db_connector = DatabaseConnector()

        league_id = "1"  # TODO test value, replace with endpoint argument
        db_connector.cursor.execute('SELECT * FROM games WHERE leagueID = '+str(league_id))  # TODO filter out games from the past
        games = db_connector.cursor.fetchall()

        schedule_data = {}

        for game in games:
            schedule_data[game[0]] = {
                "game_id" : game[0],
                "home_team_id" : game[2],
                "away_team_id" : game[3],
                "gametime" : game[5],
                "field" : game[6],
                "iscancelled" : game[7]
            }

        return schedule_data, 200

    def post(self):
        # TODO generate schedule for league
        # 1. generate play order for teams in league
        # 2. match play order with field/time pairs given by client
        # 3. generate db data
        print("post request hit")
        print(request.form)
        x = request.form['data']
        print(request.form)
        LeagueSchedule.schedule = x
        return {"schedule": self.schedule}

    def update(self):
        # TODO update schedule information for a game
        return


class PlayerSchedule(Resource):
    def get(self):
        db_connector = DatabaseConnector()

        league_id = "1"  # TODO test value, replace with endpoint argument
        player_id = "1"  # TODO ^
        db_connector.cursor.execute(
            'select * from games where leagueID = '+str(league_id)+' and (homeTeamID in (select teamID from players where playerID = '+str(player_id)+') or awayTeamID in (select teamID from players where playerID = '+str(player_id)+'));')  # TODO filter out games from the past
        games = db_connector.cursor.fetchall()

        schedule_data = {}

        for game in games:
            schedule_data[game[0]] = {
                "game_id": game[0],
                "home_team_id": game[2],
                "away_team_id": game[3],
                "gametime": game[5],
                "field": game[6],
                "iscancelled": game[7]
            }

        return schedule_data, 200