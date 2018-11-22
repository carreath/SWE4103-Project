#!/usr/bin/env python3
from flask import Flask, render_template, make_response
from flask_restful import Api
from flask_cors import CORS
from resources import *
import config

import sys
import os

from OpenSSL import SSL
from flask import request

import filecmp
from shutil import copyfile
from common import DatabaseMigrator

context = SSL.Context(SSL.SSLv23_METHOD)
cer = os.path.join(config.ssl_config['cer'])
key = os.path.join(config.ssl_config['key'])

app = Flask(__name__,
            static_url_path='',
            static_folder='dist',
            template_folder='dist')
api = Api(app)
cors = CORS(app)

# TODO ALL requests need to update the token if it exists. SOME requests need to validate the token permissions.
api.add_resource(HelloWorld, '/HelloWorld')  # TODO remove eventually (keep for debugging)
api.add_resource(LeagueSchedule, '/api/game-schedule')
api.add_resource(PlayerSchedule, '/api/player-schedule')
api.add_resource(TournamentSchedule, '/api/tournament-schedule')  # TODO placeholder endpoint name
api.add_resource(GameStats, "/api/game-stats/<game_id>")
api.add_resource(Player, "/api/player")
api.add_resource(TeamRoster, "/api/roster/<team_id>")
api.add_resource(League, "/api/league")
api.add_resource(Team, "/api/team")
api.add_resource(Login, "/api/login")
api.add_resource(Register, "/api/register")
api.add_resource(TokenValidation, "/api/token-check")
api.add_resource(User, "/api/user")
api.add_resource(Root, "/")


@app.errorhandler(404)
def catch_all(e):
    headers = {'Content-Type': 'text/html'}
    return make_response(render_template('index.html'), 200, headers)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == "__main__":
    db = DatabaseMigrator()
    if (db.migrate(False)):
        db.migrate(True)

    # Check that the SSL certificate exists if not run http://
    if os.path.isfile(cer) and os.path.isfile(key):
        context = (cer, key)
        app.run(host=config.app_settings['host'],
                port=config.app_settings['port'],
                ssl_context=context,
                debug=config.app_settings['debug'])
    else:
        app.run(host=config.app_settings['host'],
                port=config.app_settings['port'],
                debug=config.app_settings['debug'])
