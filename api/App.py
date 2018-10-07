from flask import Flask
from flask_restful import Api
from resources.HelloWorld import HelloWorld
from resources.GameSchedule import GameSchedule
from resources.TournamentSchedule import TournamentSchedule

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/HelloWorld')
api.add_resource(GameSchedule, '/')
api.add_resource(TournamentSchedule, '/asdf')

if __name__ == "__main__":
    app.run(debug=True)