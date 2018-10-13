from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources import *
# TODO find a way to address the project/client/dist static values
app = Flask(__name__,
            static_url_path='',
            static_folder='dist',
            template_folder='dist')
api = Api(app)
cors = CORS(app)

# TODO ALL requests need to update the token if it exists. SOME requests need to validate the token permissions.
api.add_resource(HelloWorld, '/HelloWorld')  # TODO remove eventually (keep for debugging)
api.add_resource(GameSchedule, '/api/game-schedule')  # TODO placeholder endpoint name
api.add_resource(TournamentSchedule, '/api/tournament-schedule')  # TODO placeholder endpoint name
api.add_resource(GameStats, "/api/game-stats/<game_id>")
api.add_resource(LeagueStanding, "/api/standings")
api.add_resource(PlayerStats, "/api/player-stats/<player_id>")
api.add_resource(TeamRoster, "/api/roster/<team_id>")
api.add_resource(Login, "/api/login")
api.add_resource(Register, "/api/register")
api.add_resource(TokenValidation, "/api/token-check")
api.add_resource(Root, "/")


if __name__ == "__main__":
    app.run(debug=True)
