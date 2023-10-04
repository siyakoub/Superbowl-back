import unittest
from flask import Flask
from app.models.user import User
from config import Config
from flaskext.mysql import MySQL
from app.utils.hashFunction import hash_password

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
        fetched_user = User.get_by_email_actif("john@example.com")
        self.assertIsNotNone(fetched_user)
        self.assertEqual(fetched_user.nom, "John")
        self.assertEqual(fetched_user.prenom, "Doe")
        self.assertEqual(fetched_user.adresseEmail, "john@example.com")
        self.assertEqual(fetched_user.motDePasse, "password")
        self.assertEqual(fetched_user.actif, 1)
        #print(fetched_user.dateInscription)
    # Ajoutez d'autres méthodes de test ici pour d'autres fonctionnalités de la classe User

    #def test_user_update(self):
    #    # Créez un nouvel utilisateur pour le test
    #    user = User("John", "Doe", "john@example.com", "password")

        # Modifiez les informations de l'utilisateur
    #    nom = "Johnathan"
    #    prenom = "Doe"
    #    adresseEmail = "update@example.com"
    #    motDePasse = "updated_password"

        # Appelez la méthode update pour enregistrer les modifications dans la base de données
    #    user.update_user(nom, prenom, adresseEmail, motDePasse)

        # Récupérez l'utilisateur mis à jour de la base de données
    #    updated_user = User.get_by_email_actif("update@example.com")

        # Vérifiez si les informations ont été correctement mises à jour
    #    self.assertIsNotNone(updated_user)
    #    self.assertEqual(updated_user.nom, "Johnathan")
    #    self.assertEqual(updated_user.prenom, "Doe")
    #    self.assertEqual(updated_user.adresseEmail, "update@example.com")
    #    self.assertEqual(updated_user.motDePasse, "updated_password")

    #def test_delete_user(self):
    #    user = User("Johnathan", "Doe", "update@example.com", "update_password")
    #    user.delete_user()

    #    deleteUser = User.get_by_email_actif("update@example.com")
    #    print(deleteUser)
    #    self.assertIsNone(deleteUser)

    #def test_user_desactivate(self):
    #    user = User("John", "Doe", "john@example.com", "password")
    #    user.save()
    #    user.desactivate_user()
    #    desactivate_user = User.get_by_email_inactif("john@example.com")
    #    print(desactivate_user)
    #    self.assertEqual(desactivate_user.actif, 0)

    def test_get_all_users_actif(self):
        passHash = hash_password("motdepassecompliquer")
        user = User("Atlas", "potter", "potter@example.com", passHash)
        user.save()

        users = User.get_all_users_actif()
        self.assertIsNotNone(users)
        for user in users:
            print(user.userID)
            print(user.nom)
            print(user.prenom)
            print(user.adresseEmail)
            print(user.motDePasse)
            print(user.actif)