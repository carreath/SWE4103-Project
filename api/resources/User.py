from flask_restful import Resource, abort, reqparse
from passlib.hash import pbkdf2_sha512
from datetime import datetime, timedelta
import time
from common import DatabaseConnector, TokenHandler


# Example POST request to register endpoint:
# curl -i -H "Content-Type: application/json" -X POST -d '{"email": "ntozer@unb.ca", "password": "password", "lastName": "Tozer", "firstName": "Nathan"}' -k http://localhost:5000/api/register
class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('firstName', type=str)
        parser.add_argument('lastName', type=str)
        args = parser.parse_args()

        first_name = args['firstName']
        last_name = args['lastName']
        email = args['email']
        hash_pw = pbkdf2_sha512.encrypt(args['password'], rounds=30000, salt_size=32)

        db_connector = DatabaseConnector()
        if db_connector.cursor.execute('CALL get_user("{}");'.format(email)) != 0:
            abort(409, error='email entered is already registered', email=email)

        # using create_user sp to store new user
        db_connector.cursor.callproc('create_user', [first_name, last_name, email, hash_pw])
        db_connector.conn.commit()

        # getting user_id to return to the frontend
        db_connector.cursor.execute('CALL get_user("{}");'.format(email))
        db_response = db_connector.cursor.fetchone()
        user_data = {
            'user_id': db_response[0],
            'privileges_id': db_response[1],
            'user_type': db_response[2],
            'first_name': db_response[3],
            'last_name': db_response[4],
            'email': db_response[5],
            'hash': db_response[6],
            'last_login': db_response[7]
        }
        db_connector.conn.close()

        return {"user": user_data}, 201


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        email = args['email']
        password = args['password']

        db_connector = DatabaseConnector()
        if db_connector.cursor.execute('CALL get_user("{}");'.format(email)) == 0:
            abort(404, error='email entered has not been registered')

        db_response = db_connector.cursor.fetchone()
        user_data = {
            'user_id': db_response[0],
            'privileges_id': db_response[1],
            'user_type': db_response[2],
            'first_name': db_response[3],
            'last_name': db_response[4],
            'email': db_response[5],
            'hash': db_response[6],
            'last_login': (db_response[7].strftime('%Y-%m-%d %H:%M:%S') if db_response[7] else "None")  # TODO make sure this solution works
        }
        if not pbkdf2_sha512.verify(password, user_data['hash']):
            abort(403, error='the password entered is incorrect')

        # update last login in database
        update_stmt = 'UPDATE users SET lastLogin = "{}" WHERE email = "{}"'
        db_connector.cursor.execute(update_stmt.format(time.strftime('%Y-%m-%d %H:%M:%S'), email))
        db_connector.conn.commit()
        db_connector.conn.close()

        # creating validation token
        token_payload = {
            'sub': email,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }
        token_handler = TokenHandler()
        token = token_handler.create_token(token_payload)

        return {'token': token.decode('UTF-8'), 'user': user_data}, 201


class TokenValidation(Resource):
    def post(self):
        # TODO
        # input : token (defined above)
        #
        return
