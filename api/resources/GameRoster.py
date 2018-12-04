from flask_restful import Resource, reqparse, abort, request
from common import DatabaseConnector, PrivilegeHandler

class GameRoster(Resource):
    # get roster for entire game
    def get(self, game_id):
        """
        Gets team roster from the database.

        :return: The list of all active players on a team

            .. code-block:: javascript

                {
                    'game-roster': {
                        'home': The home teams game roster
                        'away': The away teams game roster
                    }
                }


            Roster JSON object:

            .. code-block:: javascript

                List (of  player JSON objects)

            Player JSON object:

            .. code-block:: javascript

                {
                    'playerID': Integer,
                    'teamID': Integer,
                    'firstName': String,
                    'lastName': String,
                    'email': String,
                    'number': Integer,
                    'loanedGames': Integer
                }


        Success gives status code 200

        """
        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('get_game_roster', [game_id])
        roster = db_connector.cursor.fetchall()
        db_connector.conn.close()
        home_roster = []
        away_roster = []
        for player in roster:
            playerObj = {
                'playerID': player[0],
                'firstName': player[1],
                'lastName': player[2],
                'email': player[3],
                'loanedGames': player[4],
                'teamID': player[6],
                'number': player[8],
                'goals': player[9],
                'cleanSheet': player[10],
                'yellowCards': player[11],
                'redCards': player[12]
            }

            if playerObj['teamID'] == player[13]:
                home_roster.append(playerObj)
            else:
                away_roster.append(playerObj)

        return {"game-roster": {"home": home_roster, "away": away_roster}}

    # Post method to add a teams roster to a game
    def post(self, game_id):
        """
        Adds a roster to the database.

        :Input:  JSON object representing the game-roster

            .. code-block:: javascript

                {
                    "playerID": int,
                    "teamID": int,
                    "number": int,
                    "goals": int,
                    "cleanSheet": int,
                    "yellowCards": int,
                    "redCards": int
                }


        Success gives status code 201

        """

        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.assign_player():
            abort(403, error="Unauthorized Access (invalid permissions)")

        parser = reqparse.RequestParser()

        parser.add_argument('playerID', type=int)
        parser.add_argument('teamID', type=int)
        parser.add_argument('number', type=int)
        parser.add_argument('goals', type=int)
        parser.add_argument('cleanSheet', type=int)
        parser.add_argument('yellowCards', type=int)
        parser.add_argument('redCards', type=int)

        args = parser.parse_args()

        player_id = args['playerID']
        team_id = args['teamID']
        number = args['number']
        goals = args['goals']
        clean_sheet = args['cleanSheet']
        yellow_cards = args['yellowCards']
        red_cards = args['redCards']

        # creating new league in the database
        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('get_game_team_lineup', [int(game_id)])
        team_lineup = db_connector.cursor.fetchall()[0]

        if team_id != team_lineup[0] and team_id != team_lineup[1]:
            abort(400, error="Team " + str(team_id) + " is not playing in game " + str(game_id))

        try:
            db_connector.cursor.callproc('create_game_member', [int(game_id), player_id, team_id, number, goals, clean_sheet, yellow_cards, red_cards])
        except Exception as e:
            abort(400, error=str(e))

        db_connector.conn.commit()
        db_connector.cursor.close()

        gameMember_data = {
            'gameID': int(game_id),
            'playerID': player_id,
            'teamID': team_id,
            'number': number,
            'goals': goals,
            'cleanSheet': clean_sheet,
            'yellowCards': yellow_cards,
            'redCards': red_cards
        }

        return {'gameMember': gameMember_data}, 201

    # Put method to edit a teams roster to a game
    def put(self, game_id):
        """
        Adds a roster to the database.

        :Input:  JSON object representing the game-roster

            .. code-block:: javascript

                {
                    "playerID": int,
                    "teamID": int,
                    "number": int,
                    "goals": int,
                    "cleanSheet": int,
                    "yellowCards": int,
                    "redCards": int
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

        parser.add_argument('playerID', type=int)
        parser.add_argument('teamID', type=int)
        parser.add_argument('number', type=int)
        parser.add_argument('goals', type=int)
        parser.add_argument('cleanSheet', type=int)
        parser.add_argument('yellowCards', type=int)
        parser.add_argument('redCards', type=int)

        args = parser.parse_args()

        player_id = args['playerID']
        team_id = args['teamID']
        number = args['number']
        goals = args['goals']
        clean_sheet = args['cleanSheet']
        yellow_cards = args['yellowCards']
        red_cards = args['redCards']

        # creating new league in the database
        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('get_game_team_lineup', [int(game_id)])
        team_lineup = db_connector.cursor.fetchall()[0]

        if team_id != team_lineup[0] and team_id != team_lineup[1]:
            abort(400, error="Team " + str(team_id) + " is not playing in game " + str(game_id))

        try:
            db_connector.cursor.callproc('update_game_member',
                                         [int(game_id), player_id, team_id, number, goals, clean_sheet,
                                          yellow_cards, red_cards])
        except Exception as e:
            abort(400, error=str(e))

        db_connector.conn.commit()
        db_connector.cursor.close()

        gameMember_data = {
            'gameID': int(game_id),
            'playerID': player_id,
            'teamID': team_id,
            'number': number,
            'goals': goals,
            'cleanSheet': clean_sheet,
            'yellowCards': yellow_cards,
            'redCards': red_cards
        }

        return {'gameMember': gameMember_data}, 201

    # Delete method to delete a teams roster to a game
    def delete(self, game_id):
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        privilege_handler = PrivilegeHandler(token)
        if not privilege_handler.league_privileges():
            abort(403, error="Unauthorized Access (invalid permissions)")

        player_id = request.args.get("player_id")

        # creating new league in the database
        db_connector = DatabaseConnector()
        try:
            db_connector.cursor.callproc('delete_game_member', [int(game_id), player_id])
        except Exception as e:
            abort(400, error=str(e))

        db_connector.conn.commit()
        db_connector.cursor.close()

        return 'gameMember (' + str(game_id) + ", " + str(player_id) + ") has been deleted", 200
