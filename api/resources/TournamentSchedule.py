from flask_restful import Resource
from flask import request


class TournamentSchedule(Resource):
    schedule = "no"

    def get(self):
        return self.schedule

    def post(self):
        TournamentSchedule.schedule = request.form["data"]
