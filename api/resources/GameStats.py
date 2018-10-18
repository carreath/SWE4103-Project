from flask_restful import Resource


class GameStats(Resource):
    def get(self, game_id):
        return {"gamestats": game_id}  # TODO implement

    def post(self, game_id, data):
        #  TODO post data to db for game id
        print(data)
