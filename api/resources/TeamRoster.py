from flask_restful import Resource
from common import DatabaseConnector, PrivilegeHandler


class TeamRoster(Resource):
    def get(self, team_id):
        """
        Gets team roster from the database.

        :return: The list of all active players on a team

            .. code-block:: javascript

                {
                    'roster': List (of  Player JSON objects)
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
                    'loanedGames': Integer
                }


        Success gives status code 200

        """
        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('get_team_roster', [team_id])
        roster = db_connector.cursor.fetchall()
        db_connector.conn.close()
        roster_data = []
        print (roster)
        for player in roster:
            roster_data.append({
                'playerID': player[0],
                'teamID': player[1],
                'firstName': player[2],
                'lastName': player[3],
                'email': player[4],
                'number': player[5],
                'loanedGames': player[6]
            })
        return {'Team' + team_id: roster_data}, 200
