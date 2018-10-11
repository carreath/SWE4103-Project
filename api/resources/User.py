from flask_restful import Resource, abort, reqparse
from passlib.hash import pbkdf2_sha512
import json
from common import DatabaseConnector

parser = reqparse.RequestParser()


class User(Resource):
    def get(self):
        parser.add_argument('data', type=str)
        args = parser.parse_args()
        data = json.loads(args.data)

        email = data['username']
        password = data['password']

        db_connector = DatabaseConnector()
        if db_connector.cursor.execute('SELECT hash FROM users WHERE email = "{}"'.format(email)) == 0:
            abort(404, error='email entered has not been registered')

        user_hash = db_connector.cursor.fetchone()[0]
        if not pbkdf2_sha512.verify(password, user_hash):
            abort(403, error='the password entered is incorrect')

        return {"userID": "gottem"}, 200

    def post(self):
        parser.add_argument('data', type=str)
        args = parser.parse_args()
        data = json.loads(args.data)

        user_type = data['userType']
        first_name = data['firstName']
        last_name = data['lastName']
        email = data['email']
        hash_pw = pbkdf2_sha512.encrypt(data['password'], rounds=30000, salt_size=32)

        db_connector = DatabaseConnector()
        if db_connector.cursor.execute('SELECT * FROM users WHERE email = "{}"'.format(email)) != 0:
            abort(409, error='email entered is already registered', email=email)

        # using create_user sp to store new user
        db_connector.cursor.callproc('create_user', [user_type, first_name, last_name, email, hash_pw])
        db_connector.conn.commit()

        # getting user_id to return to the frontend
        db_connector.cursor.execute('SELECT userID FROM users WHERE email = "{}"'.format(email))
        user_id = db_connector.cursor.fetchone()[0]
        db_connector.conn.close()

        return {"userID": user_id}, 201
