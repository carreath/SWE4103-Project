from flask_restful import Resource
from flask import request


class GameSchedule(Resource):
    schedule = "hmm"

    def get(self):
        # grab schedule from DB
        return {"schedule": self.schedule}

    def put(self):
        self.schedule = request.form['data']
        return {"schedule": self.schedule}
