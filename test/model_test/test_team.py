import unittest
from flask import Flask
from app.models.team import Team
from config import Config
from flaskext.mysql import MySQL

app = Flask(__name__)


class TestTeam(unittest.TestCase):

    def setUp(self):
        # Configuration de la base de données MySQL
        app.config['MYSQL_DATABASE_HOST'] = Config.MYSQL_HOST
        app.config['MYSQL_DATABASE_USER'] = Config.MYSQL_USER
        app.config['MYSQL_DATABASE_PASSWORD'] = Config.MYSQL_PASSWORD
        app.config['MYSQL_DATABASE_DB'] = Config.MYSQL_DB

        # Initialisation de l'extension Flask-MySQL
        self.mysql = MySQL()
        self.mysql.init_app(app)

        # Créez un contexte d'application pour les tests
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

        # Créez une connexion à la base de données dans le contexte de test
        self.connection = self.mysql.connect()
        self.cursor = self.connection.cursor()

    def tearDown(self):
        # Fermez la connexion à la base de données de test ici si nécessaire
        self.cursor.close()
        self.connection.close()
        self.app_context.pop()

    #def test_create_team(self):
    #    team = Team("Chiefs de Kansas City", "USA")
    #    team.save()

    #def test_get_team_by_id(self):
    #    team = Team.get_equipe_by_id(1)
    #    self.assertIsNotNone(team)
    #    print(team.teamID)
    #    print(team.name)
    #    print(team.country)
    #    self.assertEqual(team.teamID, 1)
    #    self.assertEqual(team.name, "Eagles de Philadelphie")
    #    self.assertEqual(team.country, "USA")

    #def test_get_team_by_name(self):
    #    team = Team.get_team_by_name("Eagles de Philadelphie")
    #    self.assertIsNotNone(team)
    #    print(team.teamID)
    #    print(team.name)
    #    print(team.country)
    #    self.assertEqual(team.teamID, 1)
    #    self.assertEqual(team.name, "Eagles de Philadelphie")
    #    self.assertEqual(team.country, "USA")

    def test_get_all_teams(self):
        teams = Team.get_all_team()
        self.assertIsNotNone(teams)
        for team in teams:
            print(team.teamID)
            print(team.name)
            print(team.country)
