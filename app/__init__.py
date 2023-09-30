from flask import Flask
from flaskext.mysql import MySQL
from config import Config

app = Flask(__name__)

# Configuration de la base de données MySQL
app.config['MYSQL_DATABASE_HOST'] = Config.MYSQL_HOST
app.config['MYSQL_DATABASE_USER'] = Config.MYSQL_USER
app.config['MYSQL_DATABASE_PASSWORD'] = Config.MYSQL_PASSWORD
app.config['MYSQL_DATABASE_DB'] = Config.MYSQL_DB

# Initialisation de l'extension Flask-MySQL
mysql = MySQL()
mysql.init_app(app)


# Importez vos routes et configurez-les ici
from app import routes