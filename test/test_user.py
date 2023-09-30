import unittest

from flask import Flask

from app.models.user import User
from config import Config
from flaskext.mysql import MySQL

app = Flask(__name__)

class TestUser(unittest.TestCase):
    def setUp(self):
        # Configuration de la base de données MySQL
        app.config['MYSQL_DATABASE_HOST'] = Config.MYSQL_HOST
        app.config['MYSQL_DATABASE_USER'] = Config.MYSQL_USER
        app.config['MYSQL_DATABASE_PASSWORD'] = Config.MYSQL_PASSWORD
        app.config['MYSQL_DATABASE_DB'] = Config.MYSQL_DB

        # Initialisation de l'extension Flask-MySQL
        mysql = MySQL()
        mysql.init_app(app)


    def tearDown(self):
        # Vous pouvez fermer la connexion à la base de données de test ici si nécessaire
        pass

    def test_user_creation(self):
        # Testez la création d'un utilisateur
        user = User("John", "Doe", "john@example.com", "password")
        user.save()

        # Vérifiez si l'utilisateur a été correctement enregistré dans la base de données
        fetched_user = User.get_by_id(user.userID)
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.nom, "John")
        self.assertEqual(fetched_user.prenom, "Doe")
        self.assertEqual(fetched_user.adresseEmail, "john@example.com")
        self.assertEqual(fetched_user.motDePasse, "password")

    # Ajoutez d'autres méthodes de test ici pour d'autres fonctionnalités de la classe User
