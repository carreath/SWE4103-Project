from flask_restful import Resource, abort, reqparse, request
from common import DatabaseConnector, TokenHandler, PrivilegeHandler


class League(Resource):
    def post(self):
        """
        Adds a new league to the database.

        .. todo::
            Privileges associated with token

            .. code-block:: python

                token = request.headers.get('Authorization')
                if not token:
                    abort(403, error="Unauthorized Access (no token)")



        :Input:  JSON object representing the league

            .. code-block:: javascript

                {
                    'leagueName': String,
                    'season': String
                }



        :return: The league object that was created

            .. code-block:: javascript

                {
                    'leagueName': String,
                    'season': String
                }


        Success gives status code 201


        """
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
        """
        Gets all league records from the database.

        :return: The list of all leagues

            .. code-block:: javascript

                {
                    'leagues': List (of League JSON objects)
                }


            League JSON object:

            .. code-block:: javascript

                {
                    'leagueID': Integer,
                    'managerID': Integer,
                    'leagueName': String,
                    'season': String
                }


        Success gives status code 200

        """
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

    def delete(self):
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.assign_privileges(): # I'm using this as a placeholder for a general admin privilege
            abort(403, error="Unauthorized Access (invalid permissions)")

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
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.league_privileges():  # I'm using this as a placeholder for a general admin privilege
            abort(403, error="Unauthorized Access (invalid permissions)")

        parser = reqparse.RequestParser()
        parser.add_argument('leagueID', type=int, required=True)
        parser.add_argument('managerID', type=int)
        parser.add_argument('leagueName', type=str)
        parser.add_argument('season', type=str)
        parser.add_argument('pointScheme', type=str)

        args = parser.parse_args()
        manager = args['managerID']
        leagueID = args['leagueID']
        leagueName = args['leagueName']
        season = args['season']
        pointScheme = args['pointScheme']

        #if manager == -1:
        #    manager = 'NULL'
        #else:
        #    manager = str(manager)

        #query = "UPDATE leagues SET coordinatorID = %s, leagueName = '%s', season = '%s', pointScheme = '%s' WHERE leagueID = %d" \
        #        % (manager, args['leagueName'].strip("'"), args['season'].strip("'"), args['pointScheme'].strip("'"), args['leagueID'])

        db = DatabaseConnector()
        db.cursor.callproc('update_league',
                           [leagueID,
                            leagueName,
                            season,
                            pointScheme,
                            manager])
        db.conn.commit()
        return 200