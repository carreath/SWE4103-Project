import jwt
from flask_restful import abort
import config
from common import DatabaseConnector


class TokenHandler:
    def __init__(self):
        self.secret = config.jwt_secret

    def create_token(self, payload):
        return jwt.encode(payload=payload, key=self.secret, algorithm='RS256')

    def decode_token(self, token):
        try:
            payload = jwt.decode(jwt=token, key=self.secret, algorithm='RS256')
            user = payload['sub']
            if not user:
                raise RuntimeError('User not found')
            return user
        except jwt.ExpiredSignatureError:
            abort(401, error='Expired token, authentication required.', authentication=False)
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            abort(401, error='Invalid token, registration and/or authentication required.', authentitication=False)

    def get_token_user(self, token):
        db_connector = DatabaseConnector()
        user = self.decode_token(token)
        if not user:
            raise RuntimeError('User not found')  # might be a better way to throw this error
        if db_connector.cursor.execute('CALL get_user("{}");'.format(user)) == 0:
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
            'last_login': (db_response[7].strftime('%Y-%m-%d %H:%M:%S') if db_response[7] else "None")
        # TODO make sure this solution works properly (fixes 500 NoneType on first login)
        }
        db_connector.conn.close()
        return user_data
