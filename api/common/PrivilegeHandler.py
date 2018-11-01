from common import TokenHandler
from common import DatabaseConnector


class PrivilegeHandler:
    def __init__(self, token):
        tk_handler = TokenHandler()
        db_connector = DatabaseConnector()
        user_email = tk_handler.decode_token(token)
        db_connector.cursor.execute('CALL get_user("{}");'.format(user_email))
        db_response = db_connector.cursor.fetchone()
        privilege_id = db_response[1]
        if privilege_id is None:
            self.privileges = None
            db_connector.conn.close()
        else:
            db_connector.cursor.execute('CALL get_privileges({});'.format(privilege_id))
            db_response = db_connector.cursor.fetchone()
            self.privileges = {
                'privileges_type': db_response[1],
                'cancel_game': db_response[2],
                'update_score': db_response[3],
                'create_player': db_response[4],
                'create_game': db_response[5],
                'create_user': db_response[6],
                'create_team': db_response[7],
                'create_league': db_response[8],
                'assign_player': db_response[9],
                'assign_manager': db_response[10],
                'assign_coordinator': db_response[11],
                'assign_privileges': db_response[12]
            }
            db_connector.conn.close()
