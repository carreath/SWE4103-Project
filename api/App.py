from flask import Flask
from flask_restful import Api
from resources.HelloWorld import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/HelloWorld')

if __name__ == "__main__":
    app.run(debug=True)