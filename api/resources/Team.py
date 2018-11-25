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
                    'draws': Integer,
                    'gamesPlayed': Integer,
                    'goalsFor': Integer,
                    'goalsAgainst': Integer,
                    'goalsDifference': Integer,
                    'cleanSheets': Integer,
                    'yellowCards': Integer,
                    'redCards': Integer
                }


        Possible status codes: 200 = Success.

        """

        db_connector = DatabaseConnector()
        db_connector.cursor.callproc('get_all_teams')

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
                'goalsFor': team[9],
                'goalsAgainst': 0,
                'cleanSheets': team[10],
                'yellowCards': team[11],
                'redCards': team[12]
            })

        # getting team statistics
        query = 'SELECT g.teamID, g.gameID, CAST(SUM(g.goals) AS INT) FROM gameMembers g GROUP BY g.gameID, g.teamID;'
        db_connector.cursor.execute(query)
        goals_data = db_connector.cursor.fetchall()
        teams = []
        games = []
        goals = []
        for row in goals_data:
            teams.append(row[0])
            goals.append(row[2])
            games.append(row[1])
        goals_against = {}

        for team_id in set(teams):
            goals_against[team_id] = 0
            games_played = []
            for i in range(len(games)):
                if teams[i] == team_id:
                    games_played.append(games[i])
            for i in range(len(teams)):
                if games[i] in games_played and teams[i] != team_id:
                    goals_against[team_id] += goals[i]

        for team in teams_data:
            team['goalsAgainst'] = goals_against[team['teamID']]
            team['goalDifference'] = team['goalsFor'] - team['goalsAgainst']
            team['gamesPlayed'] = team['wins'] + team['losses'] + team['draws']

        # calculating league points
        for team in teams_data:
            query = 'SELECT pointScheme FROM leagues WHERE leagueID = {}'.format(team['leagueID'])
            db_connector.cursor.execute(query)
            point_scheme = db_connector.cursor.fetchone()[0]
            if point_scheme == 'Capital Scoring':
                team['pointScheme'] = 1 * team['wins'] + 0 * team['draw'] - 1 * team['losses']
            elif point_scheme == 'Standard':
                team['pointScheme'] = 3 * team['wins'] + 1 * team['draw'] + 0 * team['losses']

        db_connector.conn.close()
        print(teams_data[0])
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
            'leagueID': db_response[1],
            'managerID': db_response[2],
            'teamName': db_response[3],
            'colour': db_response[4],
            'leaguePoints': db_response[5],
            'wins': db_response[6],
            'losses': db_response[7],
            'draws': db_response[8]
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
        try:
            db_connector.cursor.execute('DELETE FROM teams WHERE teamID = {}'.format(team_id))
            db_connector.conn.commit()
        except Exception as e:
            abort(401, error='Invalid delete: {}'.format(e))
        finally:
            db_connector.conn.close()

        return 200
