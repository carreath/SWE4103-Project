import jwt
from flask_restful import abort
import config
from datetime import datetime, timedelta


class TokenHandler:
    """
    TokenHandler is for handling tokens
    """
    def __init__(self):
        """
        This is just the constructor
        """
        self.secret = config.jwt_secret

    def create_token(self, email):
        """
        Creates a token from a user email

        :param email: User email (String)

        :return: JSON Web Token (String) with the user email encoded inside

        """
        token_payload = {
            'sub': email,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=120)
        }
        return jwt.encode(payload=token_payload, key=self.secret, algorithm='HS256')

    def decode_token(self, token):
        """
        Decodes from a token to a user email

        :param token: JSON Web Token (String)

        :return: User email (String)

        Aborts with a 401 if no token is passed in or the token is expired
        """
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
        """
        Creates a new refreshed token

        :param token: JSON Web Token (String)

        :return: JSON Web Token (String) with a refreshed expiration date

        """
        email = self.decode_token(token)
        return self.create_token(email)
