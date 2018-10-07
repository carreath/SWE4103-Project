from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
mariadb = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'leagues'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mariadb.init_app(app)

conn = mariadb.connect()
cursor = conn.cursor()

cursor.execute("SELECT * FROM leagues")
