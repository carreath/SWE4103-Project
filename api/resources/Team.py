from flask_restful import Resource, abort, reqparse, request
from common import DatabaseConnector, TokenHandler


class Team(Resource):
    def post(self):
        """
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        """
        # TODO privileges associated with token

        parser = reqparse.RequestParser()

        parser.add_argument('teamName', type=str)
        parser.add_argument('colour', type=str)
        parser.add_argument('leaguePoints', type=int)
        parser.add_argument('wins', type=int)
        parser.add_argument('losses', type=int)
        parser.add_argument('draws', type=int)

        args = parser.parse_args()

        team_name = args['teamName']
        colour = args['colour']
        league_points = args['leaguePoints']
        wins = args['wins']
        losses = args['losses']
        draws = args['draws']

        # creating new league in the database
        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('create_team', [team_name, colour, league_points, wins, losses, draws])
        db_connector.conn.commit()
        db_connector.cursor.close()

        team_data = {
            'team_name': team_name,
            'colour': colour,
            'league_points': league_points,
            'wins': wins,
            'losses': losses,
            'draws': draws
        }

        return {'team': team_data}, 201

    def get(self):
        db_connector = DatabaseConnector()
        db_connector.cursor.execute('SELECT * FROM teams')

        teams = db_connector.cursor.fetchall()
        teams_data = {}

        for team in teams:
            teams_data[team[0]] = {
                'team_id': team[0],
                'league_id': team[1],
                'manager_id': team[2],
                'team_name': team[3],
                'colour': team[4],
                'league_points': team[5],
                'wins': team[6],
                'losses': team[7],
                'draws': team[8],
            }

        return teams_data, 200
