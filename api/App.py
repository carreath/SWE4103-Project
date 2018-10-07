from flask import Flask
from flask_restful import Api
from resources import *
app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/HelloWorld')  # TODO remove eventually (keep for debugging)
api.add_resource(GameSchedule, '/game-schedule')  # TODO placeholder endpoint name
api.add_resource(TournamentSchedule, '/tournament-schedule')  # TODO placeholder endpoint name
api.add_resource(GameStats, "/game-stats/<game_id>")
api.add_resource(LeagueStanding, "/standings")
api.add_resource(PlayerStats, "/player-stats/<player_id>")
api.add_resource(TeamRoster, "/roster/<team_id>")


if __name__ == "__main__":
    app.run(debug=True)
