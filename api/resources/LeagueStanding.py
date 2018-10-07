from flask_restful import Resource

class LeagueStanding(Resource):
    def get(self):
        return {"LeagueStandings": [(1, "Team1"), (2, "BestTeam")]}  # TODO implement
