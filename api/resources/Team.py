from flask_restful import Resource, abort, reqparse, request
from common import DatabaseConnector, TokenHandler, PrivilegeHandler


class Team(Resource):
    def post(self):
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.team_privileges():
            abort(403, error="Unauthorized Access (invalid permissions)")

        parser = reqparse.RequestParser()

        parser.add_argument('teamName', type=str)
        parser.add_argument('leagueID', type=int)
        parser.add_argument('colour', type=str)

        args = parser.parse_args()

        team_name = args['teamName']
        league_id = args['leagueID']
        colour = args['colour']

        # creating new league in the database
        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('create_team', [team_name, league_id, colour])
        db_connector.conn.commit()
        db_connector.cursor.close()

        team_data = {
            'teamName': team_name,
            'leagueID': league_id,
            'colour': colour
        }

        return {'team': team_data}, 201

    def get(self):
        db_connector = DatabaseConnector()
        db_connector.cursor.execute('SELECT * FROM teams')

        teams = db_connector.cursor.fetchall()
        teams_data = []
        for team in teams:
            teams_data.append({
                'teamID': team[0],
                'leagueID': team[1],
                'managerID': team[2],
                'teamName': team[3],
                'colour': team[4],
                'leaguePoints': team[5],
                'wins': team[6],
                'losses': team[7],
                'draws': team[8],
            })
        return {'teams': teams_data}, 200
