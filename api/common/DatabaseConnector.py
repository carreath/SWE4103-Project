from flask import Flask
from flaskext.mysql import MySQL
import config


class DatabaseConnector:
    def __init__(self):
        app = Flask(__name__)
        mariadb = MySQL()

        app.config['MYSQL_DATABASE_USER'] = config.aws_db['user']
        app.config['MYSQL_DATABASE_PASSWORD'] = config.aws_db['password']
        app.config['MYSQL_DATABASE_DB'] = config.aws_db['database']
        app.config['MYSQL_DATABASE_HOST'] = config.aws_db['host']
        app.config['MYSQL_DATABASE_PORT'] = config.aws_db['port']

        mariadb.init_app(app)

        self.conn = mariadb.connect()
        self.cursor = self.conn.cursor()


# TODO remove this when there are more robust database access examples
if __name__ == "__main__":
    select_stmt = (
        'SHOW COLUMNS FROM users'
    )

    db_conn = DatabaseConnector()
    result = db_conn.cursor.execute(select_stmt)
    row = db_conn.cursor.fetchone()
    while row is not None:
        print(row)
        row = db_conn.cursor.fetchone()
    print('{} rows accessed'.format(result))
