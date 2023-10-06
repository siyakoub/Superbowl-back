import time
import unittest
from flask import Flask
from app.models.admin import Admin
from config import Config
from flaskext.mysql import MySQL


app = Flask(__name__)


class TestAdmin(unittest.TestCase):

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

    #def test_create_admin(self):
    #    admin = Admin("siyakoubm", "1mourad2", "Si Yakoub", "Mourad")
    #    admin.save()
    #    fetched_admin = Admin.get_admin_actif_by_login("siyakoubm")
    #    self.assertIsNotNone(fetched_admin)
    #    print(fetched_admin.adminID)
    #    print(fetched_admin.login)
    #    print(fetched_admin.password)
    #    print(fetched_admin.nom)
    #    print(fetched_admin.prenom)
    #    print(fetched_admin.actif)
    #    self.assertEqual(fetched_admin.adminID, 1)
    #    self.assertEqual(fetched_admin.login, "siyakoubm")
    #    self.assertEqual(fetched_admin.password, "1mourad2")
    #    self.assertEqual(fetched_admin.nom, "Si Yakoub")
    #    self.assertEqual(fetched_admin.prenom, "Mourad")
    #    self.assertEqual(fetched_admin.actif, 1)
    #    time.sleep(5)

    #def test_update_admin(self):
    #    admin = Admin.get_admin_actif_by_login("siyakoubm")
    #    login = "siyakoubmourad"
    #    password = "update_password"
    #    nom = "siyakoub"
    #    prenom = "mourad"

    #    time.sleep(1)

    #    admin.update_admin(login, password, nom, prenom)
    #    newAdminInfo = Admin.get_admin_actif_by_login("siyakoubmourad")
    #    self.assertEqual(newAdminInfo.adminID, 1)
    #    self.assertEqual(newAdminInfo.login, "siyakoubmourad")
    #    self.assertEqual(newAdminInfo.password, "update_password")
    #    self.assertEqual(newAdminInfo.nom, "siyakoub")
    #    self.assertEqual(newAdminInfo.prenom, "mourad")
    #    self.assertEqual(newAdminInfo.actif, 1)

    #def test_desactivate_admin(self):
    #    admin = Admin.get_admin_actif_by_login("siyakoubmourad")
    #    admin.desactivate_admin()
    #    inactif_admin = Admin.get_admin_inactif_by_login("siyakoubmourad")
    #    self.assertEqual(inactif_admin.actif, 0)

    def test_delete_admin(self):
        admin = Admin.get_admin_by_login("siyakoubmourad")
        admin.delete_admin()
        supp_admin = Admin.get_admin_by_login("siyakoubmourad")
        self.assertIsNone(supp_admin)