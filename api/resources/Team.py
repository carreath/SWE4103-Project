from flask_restful import Resource, abort, reqparse, request
from common import DatabaseConnector, PrivilegeHandler


class Team(Resource):
    """
    This endpoint allows access to the teams table records.

    """
    def post(self):
        """
        Adds a new team to the database.

        :Input:  JSON object representing the team

            .. code-block:: javascript

                {
                    'teamName': String,
                    'leagueID': Integer,
                    'colour': String (Hex Colour Code)
                }



        :return: The team object that was created

            .. code-block:: javascript

                {
                    'teamName': String,
                    'leagueID': Integer,
                    'colour': String (Hex Colour Code)
                }


        Possible status codes: 403 = No permissions, 201 = Successfully added.


        """        
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
        """
        Gets all team records from the database.

        :return: The list of all teams

            .. code-block:: javascript

                {
                    'teams': List (of Team JSON objects)
                }


            Team JSON object:

            .. code-block:: javascript

                {
                    'teamID': Integer,
                    'leagueID': Integer,
                    'managerID': Integer,
                    'teamName': String,
                    'colour': String (Hex Colour Code),
                    'leaguePoints': Integer,
                    'wins': Integer,
                    'losses': Integer,
                    'draws': Integer
                }


        Possible status codes: 200 = Success.

        """

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

    def put(self):
        """
        Updates a team object in the database.

        :Input:  Team JSON object with new data.

            .. code-block:: javascript

                {
                    'teamID': Integer,
                    'leagueID': Integer,
                    'managerID': Integer,
                    'teamName': String,
                    'colour': String (Hex Colour Code),
                    'leaguePoints': Integer,
                    'wins': Integer,
                    'losses': Integer,
                    'draws': Integer
                }


        :return: The updated team JSON object

            .. code-block:: javascript

                {
                    'teamID': Integer,
                    'leagueID': Integer,
                    'managerID': Integer,
                    'teamName': String,
                    'colour': String (Hex Colour Code),
                    'leaguePoints': Integer,
                    'wins': Integer,
                    'losses': Integer,
                    'draws': Integer
                }


        Possible status codes: 403 = No permissions, 200 = Successfully updated.

        """

        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.team_privileges():
            abort(403, error="Unauthorized Access (invalid permissions)")

        parser = reqparse.RequestParser()
        parser.add_argument('teamID', type=int)
        parser.add_argument('leagueID', type=int)
        parser.add_argument('managerID', type=int)
        parser.add_argument('teamName', type=str)
        parser.add_argument('colour', type=str)
        parser.add_argument('leaguePoints', type=str)
        parser.add_argument('wins', type=str)
        parser.add_argument('losses', type=str)
        parser.add_argument('draws', type=str)
        args = parser.parse_args()

        team_id = args['teamID']
        league_id = args['leagueID']
        manager_id = args['managerID']
        team_name = args['teamName']
        colour = args['colour']
        league_points = args['leaguePoints']
        wins = args['wins']
        losses = args['losses']
        draws = args['draws']

        # using update_team stored procedure to update team
        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('update_team',
                                     [team_id,
                                      league_id,
                                      manager_id,
                                      team_name,
                                      colour,
                                      league_points,
                                      wins,
                                      losses,
                                      draws])
        db_connector.conn.commit()

        # getting team_id to return to the frontend
        db_connector.cursor.callproc('get_team', [team_id])
        db_response = db_connector.cursor.fetchone()
        team_data = {
            'teamID': db_response[0],
            'leagueID': db_response[2],
            'managerID': db_response[3],
            'teamName': db_response[4],
            'colour': db_response[5],
            'leaguePoints': db_response[6],
            'wins': db_response[7],
            'losses': db_response[8],
            'draws': db_response[9]
        }
        db_connector.conn.close()

        return team_data, 200

    def delete(self):
        """
        Deletes a team from the database.

        :Input:  ID of the team to delete.

            .. code-block:: javascript

                {
                    'teamID': Integer
                }

        Possible status codes: 403 = No permissions, 200 = Successfully deleted.

        """
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.team_privileges():
            abort(403, error="Unauthorized Access (invalid permissions)")

        parser = reqparse.RequestParser()
        parser.add_argument('teamID')
        args = parser.parse_args()

        team_id = args['teamID']

        # deleting team object
        db_connector = DatabaseConnector()
        db_connector.cursor.execute('DELETE FROM teams WHERE teamID = {}'.format(team_id))
        db_connector.conn.commit()
        db_connector.conn.close()

        return 200
