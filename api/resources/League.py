from flask_restful import Resource, abort, reqparse, request
from common import DatabaseConnector, TokenHandler, PrivilegeHandler


class League(Resource):
    def post(self):
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.league_privileges():
            abort(403, error="Unauthorized Access (invalid permissions)")

        parser = reqparse.RequestParser()
        parser.add_argument('leagueName', type=str)
        parser.add_argument('season', type=str)
        parser.add_argument('pointScheme', type=str)
        args = parser.parse_args()

        league_name = args['leagueName']
        season = args['season']
        point_scheme = args['pointScheme']

        # creating new league in the database
        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('create_league', [league_name, season, point_scheme])
        db_connector.conn.commit()
        db_connector.cursor.close()

        league_data = {
            'leagueName': league_name,
            'season': season,
            'pointScheme': point_scheme
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
                'season': league[3],
                'pointScheme': league[4]
            })

        return {'leagues': leagues_data}, 200
