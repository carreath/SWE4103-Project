from flask_restful import Resource, reqparse
from common import DatabaseConnector


class Player(Resource):
    """
    This endpoint allows access to the players table records.

    """
    def get(self):
        """
        Gets all player records from the database.

        :return: The list of all teams

            .. code-block:: javascript

                {
                    'players': List (of  Player JSON objects)
                }


            Player JSON object:

            .. code-block:: javascript

                {
                    'playerID': Integer,
                    'teamID': Integer,
                    'firstName': String,
                    'lastName': String,
                    'email': String,
                    'number': Integer,
                    'loanedGames': Integer,
                    'goals': Integer,
                    'cleanSheets': Integer,
                    'yellowCards': Integer,
                    'redCards': Integer
                }


        Success gives status code 200

        """
        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('get_players', [])
        players = db_connector.cursor.fetchall()
        db_connector.conn.close()
        players_data = []
        for player in players:
            players_data.append({
                'playerID': player[0],
                'teamID': player[1],
                'firstName': player[2],
                'lastName': player[3],
                'email': player[4],
                'number': player[5],
                'loanedGames': player[6],
                'goals': player[7],
                'cleanSheets': player[8],
                'yellowCards': player[9],
                'redCards': player[10]
            })
        return {'players': players_data}, 200

    # TODO implement some authentication with tokens here
    def post(self):
        """
        Adds a new player to the database.

        :Input:  JSON object representing the player

            .. code-block:: javascript

                {
                    'teamID': Integer,
                    'firstName': String,
                    'lastName': String,
                    'email': String (optional),
                    'number': Integer (optional)
                }



        :return: The player object that was created

            .. code-block:: javascript

                {
                    'teamID': Integer,
                    'firstName': String,
                    'lastName': String,
                    'email': String,
                    'number': Integer
                }


        Success gives status code 201

        """
        parser = reqparse.RequestParser()
        parser.add_argument('teamID', type=int)
        parser.add_argument('firstName', type=str)
        parser.add_argument('lastName', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('number', type=int)

        args = parser.parse_args()

        team_id = args['teamID']
        first_name = args['firstName']
        last_name = args['lastName']
        email = args['email'] if args['email'] else None
        number = args['number']

        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('create_player', [team_id, first_name, last_name, email, number])
        db_connector.conn.commit()
        db_connector.conn.close()

        player = {
            'teamID': team_id,
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'number': number
        }

        return {'player': player}, 201
