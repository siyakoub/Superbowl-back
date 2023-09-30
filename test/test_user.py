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

    def test_user_creation(self):
        # Testez la création d'un utilisateur
        user = User("John", "Doe", "john@example.com", "password")
        user.save()

        # Vérifiez si l'utilisateur a été correctement enregistré dans la base de données
        fetched_user = User.get_by_email("john@example.com")
        print(fetched_user)  # Ajoutez cette ligne pour afficher fetched_user dans la console
        self.assertIsNotNone(fetched_user)
        print(fetched_user.userID)  # Imprimez userID après les autres informations
        print(fetched_user.nom)
        print(fetched_user.prenom)
        print(fetched_user.adresseEmail)
        print(fetched_user.motDePasse)
        print(fetched_user.dateInscription)
        self.assertEqual(fetched_user.userID, 5)
        self.assertEqual(fetched_user.nom, "John")
        self.assertEqual(fetched_user.prenom, "Doe")
        self.assertEqual(fetched_user.adresseEmail, "john@example.com")
        self.assertEqual(fetched_user.motDePasse, "password")
        #print(fetched_user.dateInscription)
    # Ajoutez d'autres méthodes de test ici pour d'autres fonctionnalités de la classe User
