from flask import Flask
from flaskext.mysql import MySQL
from config import Config
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

# Configuration de la base de données MySQL
app.config['MYSQL_DATABASE_HOST'] = Config.MYSQL_HOST
app.config['MYSQL_DATABASE_USER'] = Config.MYSQL_USER
app.config['MYSQL_DATABASE_PASSWORD'] = Config.MYSQL_PASSWORD
app.config['MYSQL_DATABASE_DB'] = Config.MYSQL_DB

CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000/"}})

mysql = MySQL()
mysql.init_app(app)

from app.routes import user_route, admin_route, team_route, player_route, odds_route, match_route, comment_route, bet_route, event_route, historique_mise_route, session_route

app.register_blueprint(user_route.user_bp, url_prefix='/api/user')
app.register_blueprint(admin_route.admin_bp, url_prefix='/api/admin')
app.register_blueprint(team_route.team_bp, url_prefix='/api/team')
app.register_blueprint(player_route.player_bp, url_prefix='/api/player')
app.register_blueprint(odds_route.odds_bp, url_prefix='/api/odd')
app.register_blueprint(match_route.match_bp, url_prefix='/api/match')
app.register_blueprint(comment_route.comment_bp, url_prefix='/api/comment')
app.register_blueprint(bet_route.bet_bp, url_prefix='/api/bet')
app.register_blueprint(event_route.event_bp, url_prefix='/api/event')
app.register_blueprint(historique_mise_route.historique_mise_bp, url_prefix='/api/historiquemise')
app.register_blueprint(session_route.session_bp, url_prefix='/api/session')
