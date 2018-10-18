from flask_restful import Resource
from flask import request


class GameSchedule(Resource):
    schedule = "hmm"

    def get(self):
        # grab schedule from DB
        return {"schedule": self.schedule}

    def put(self):
        print("put request hit")
        print(request.form)
        x = request.form['data']
        print(request.form)
        GameSchedule.schedule = x
        return {"schedule": self.schedule}
