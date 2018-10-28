from flask_restful import Resource


class TeamRoster(Resource):
    def get(self, team_id):
        return {"Team Roster for " + team_id: ["Player One", "Player Two"]}  # TODO implement

    def post(self, team_id, team_list):
        #  TODO create player records in db, assign to team
        print((team_id, team_list))