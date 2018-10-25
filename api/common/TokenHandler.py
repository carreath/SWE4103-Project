import jwt
from flask_restful import abort
import config
from datetime import datetime, timedelta


class TokenHandler:
    def __init__(self):
        self.secret = config.jwt_secret

    def create_token(self, email):
        token_payload = {
            'sub': email,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=120)
        }
        return jwt.encode(payload=token_payload, key=self.secret, algorithm='HS256')

    def decode_token(self, token):
        try:
            payload = jwt.decode(jwt=token, key=self.secret, algorithm='HS256')
            user = payload['sub']
            if not user:
                raise RuntimeError('User not found')
            return user
        except jwt.ExpiredSignatureError:
            abort(401, error='Expired token, authentication required.', authentication=False)
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            abort(401, error='Invalid token, registration and/or authentication required.', authentitication=False)

    def refresh_token(self, token):
        email = self.decode_token(token)
        return self.create_token(email)
