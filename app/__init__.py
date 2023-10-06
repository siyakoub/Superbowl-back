from flask import Flask
from flask_restplus import Api, Resource
from flaskext.mysql import MySQL
from config import Config


app = Flask(__name__)
api = Api(app, version='1.0', title='superBowlAPI', description='Back-end de l\'application de pari sprotif sur le '
                                                                'superBowl')

# Configuration de la base de données MySQL
app.config['MYSQL_DATABASE_HOST'] = Config.MYSQL_HOST
app.config['MYSQL_DATABASE_USER'] = Config.MYSQL_USER
app.config['MYSQL_DATABASE_PASSWORD'] = Config.MYSQL_PASSWORD
app.config['MYSQL_DATABASE_DB'] = Config.MYSQL_DB
app.config['RESTPLUS_MASK_SWAGGER'] = False

mysql = MySQL()
mysql.init_app(app)

from app.routes import user_route, admin_route, team_route, player_route

app.register_blueprint(user_route.user_bp, url_prefix='/api/user')
app.register_blueprint(admin_route.admin_bp, url_prefix='/api/admin')
app.register_blueprint(team_route.team_bp, url_prefix='/api/team')
app.register_blueprint(player_route.player_bp, url_prefix='/api/player')
