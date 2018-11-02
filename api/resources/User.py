from flask_restful import Resource, abort, reqparse, request
from passlib.hash import pbkdf2_sha512
from datetime import datetime, timedelta
import time
from common import DatabaseConnector, TokenHandler


# Example POST request to register endpoint:
# curl -i -H "Content-Type: application/json" -X POST -d '{"email": "ntozer@unb.ca", "password": "password", "lastName": "Tozer", "firstName": "Nathan"}' -k http://localhost:5000/api/register
class Register(Resource):
    """
        Endpoint for registering a new user account.
    """
    def post(self):
        """
        Adds a new user to the database with default permissions.

        :Input:  JSON object representing the new user account

            .. code-block:: javascript

                {
                    'email': String,
                    'password': String,
                    'firstName': String,
                    'lastName': String
                }



        :return: The user object that was created

            .. code-block:: javascript

                {
                    'teamName': String,
                    'leagueID': Integer,
                    'colour': String (Hex Colour Code)
                }


        Success gives status code 201

        """
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
            'user_type': db_response[2],
            'first_name': db_response[3],
            'last_name': db_response[4],
            'email': db_response[5],
            'last_login': db_response[7]
        }
        db_connector.conn.close()

        return {"user": user_data}, 201


class Login(Resource):
    """
        Endpoint for logging in.
    """
    def post(self):
        """
        Attempts to log in with the given account.

        :Input:  JSON object with the user email and password.

            .. code-block:: javascript

                {
                    'email': String,
                    'password': String
                }



        :return: The JSON Web Token and the user's data.

            .. code-block:: javascript

                {
                    'token': String (JSON Web Token),
                    'user_data':
                        {
                            'userID': Integer,
                            'userType': String,
                            'firstName': String,
                            'lastName': String,
                            'email': String,
                            'lastLogin': String
                        }
                }


        Success gives status code 201

        """
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
            'user_type': db_response[2],
            'first_name': db_response[3],
            'last_name': db_response[4],
            'email': db_response[5],
            'last_login': db_response[7].strftime('%Y-%m-%d %H:%M:%S') if db_response[7] else None
        }
        if not pbkdf2_sha512.verify(password, db_response[6]):
            abort(403, error='the password entered is incorrect')

        # update last login in database
        update_stmt = 'UPDATE users SET lastLogin = "{}" WHERE email = "{}"'
        db_connector.cursor.execute(update_stmt.format(time.strftime('%Y-%m-%d %H:%M:%S'), email))
        db_connector.conn.commit()
        db_connector.conn.close()

        # creating validation token
        token_handler = TokenHandler()
        token = token_handler.create_token(email)

        return {'token': token.decode('UTF-8'), 'user': user_data}, 201


class TokenValidation(Resource):
    """
    Endpoint for validating web tokens
    """
    # If token is valid, return refreshed token and user information. Else, return 403 error.
    def get(self):
        """
        Checks if the current web token is valid, then refreshes the token and user data.

        :Input:

            .. code-block:: javascript

                Header:
                'Authorization': String (JSON Web Token)



        :return: The refreshed JSON Web Token

            .. code-block:: javascript

                {
                    'token': String (JSON Web Token)
                }


        Success gives status code 200
        Failiure gives status code 403

        """
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        tk_handler = TokenHandler()
        new_token = tk_handler.refresh_token(token)
        return {'token': new_token.decode('UTF-8')}, 200


class User(Resource):
    """
    This endpoint allows access to the users table records.
    """
    def get(self):
        """
        Gets user data from the database.

        :Input:

            .. code-block:: javascript

                Header:
                'Authorization': String (JSON Web Token)


        :return: A JSON object containing the user data.

            .. code-block:: javascript

                {
                    'userID': Integer,
                    'userType': String,
                    'firstName': String,
                    'lastName': String,
                    'email': String,
                    'lastLogin': String
                }

        Success gives status code 200

        """
        token = request.headers.get('Authorization')
        if not token:
            abort(403, error="Unauthorized Access (no token)")
        tk_handler = TokenHandler()
        user_email = tk_handler.decode_token(token)
        db_connector = DatabaseConnector()
        # getting user_id to return to the frontend
        db_connector.cursor.execute('CALL get_user("{}");'.format(user_email))
        db_response = db_connector.cursor.fetchone()
        user_data = {
            'user_id': db_response[0],
            'user_type': db_response[2],
            'first_name': db_response[3],
            'last_name': db_response[4],
            'email': db_response[5],
            'last_login': db_response[7].strftime('%Y-%m-%d %H:%M:%S') if db_response[7] else None
        }
        db_connector.conn.close()

        return {'user': user_data}, 200