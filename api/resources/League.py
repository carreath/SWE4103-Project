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

    def delete(self):
        # TODO this desperately needs permissions implemented

        parser = reqparse.RequestParser()
        parser.add_argument('leagueID', type=int)
        args = parser.parse_args()

        target_league_id = args['leagueID']

        db = DatabaseConnector()
        db.cursor.execute("DELETE FROM gameMembers WHERE teamID in (SELECT teamID FROM teams WHERE leagueID = %d);" % target_league_id)
        db.cursor.execute("DELETE FROM games WHERE leagueID = %d;" % target_league_id)
        db.cursor.execute("DELETE FROM players WHERE teamID in (SELECT teamID FROM teams WHERE leagueID = %d);" % target_league_id)
        db.cursor.execute("DELETE FROM teams WHERE leagueID = %d;" % target_league_id)
        db.cursor.execute("DELETE FROM leagues WHERE leagueID = %d;" % target_league_id)
        db.conn.commit()
        return 200

    def put(self):
        # TODO permissions
        parser = reqparse.RequestParser()
        parser.add_argument('leagueID', type=int, required=True)
        parser.add_argument('managerID', type=int)
        parser.add_argument('leagueName', type=str)
        parser.add_argument('season', type=str)

        args = parser.parse_args()
        query = "UPDATE leagues SET coordinatorID = %d, leagueName = '%s', season = '%s' WHERE leagueID = %d" \
                % (args['managerID'], args['leagueName'], args['season'], args['leagueID'])
        db = DatabaseConnector()
        db.cursor.execute(query)
        db.conn.commit()
        return 200