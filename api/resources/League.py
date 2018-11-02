from flask_restful import Resource, abort, reqparse, request
from common import DatabaseConnector, TokenHandler


class League(Resource):
    def post(self):
        """
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        """
        # TODO privileges associated with token

        parser = reqparse.RequestParser()
        parser.add_argument('leagueName', type=str)
        parser.add_argument('season', type=str)
        args = parser.parse_args()

        league_name = args['leagueName']
        season = args['season']

        # creating new league in the database
        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('create_league', [league_name, season])
        db_connector.conn.commit()
        db_connector.cursor.close()

        league_data = {
            'leagueName': league_name,
            'season': season
        }

        return {'league': league_data}, 201

    def get(self):
        db_connector = DatabaseConnector()
        db_connector.cursor.execute('SELECT * FROM leagues')

        leagues = db_connector.cursor.fetchall()
        leagues_data = []

        for league in leagues:
            leagues_data.append({
                'leagueID': league[0],
                'managerID': league[1],
                'leagueName': league[2],
                'season': league[3]
            })

        return {'leagues': leagues_data}, 200
