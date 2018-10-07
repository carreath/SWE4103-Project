from flask_restful import Resource


class PlayerStats(Resource):
    def get(self, player_id):
        return {"playerstats": player_id}  # TODO implement
