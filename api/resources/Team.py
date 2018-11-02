from flask_restful import Resource, abort, reqparse, request
from common import DatabaseConnector, TokenHandler


class Team(Resource):
    """
    This endpoint allows access to the teams table records.

    .. Note:: This is a note (wow!)

    .. warning:: This is a warning (oh no!)

    .. todo::
        Privileges associated with token

        .. code-block:: python

            token = request.headers.get('Authorization')
            if not token:
                abort(403, error="Unauthorized Access (no token)")


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


        Success gives status code 201

        """


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


        Success gives status code 200

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
