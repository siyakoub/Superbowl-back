import os

class Config:
    # Clé secrète pour la sécurité des sessions (à personnaliser)
    SECRET_KEY = '6798dcf7beeb063cce923f03304f8437'

    # Configuration de la base de données MySQL
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1Mehdi23!'
    MYSQL_DB = 'superBowlBdd'
    MYSQL_CURSORCLASS = 'DictCursor'  # Utilisez un curseur de type dictionnaire

    # Configurations supplémentaires (à personnaliser)
    DEBUG = True  # Active le mode de débogage Flask
    UPLOAD_FOLDER = 'uploads'  # Dossier pour les téléchargements de fichiers
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limite la taille des fichiers téléchargés à 16 Mo

    # Configurations pour la sécurité des sessions
    SESSION_COOKIE_SECURE = False  # Activez cette option en production avec HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'  # Utilisez 'Strict' en production pour plus de sécurité

    # Configurations de Flask-Mail (pour l'envoi d'e-mails, le cas échéant)
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'votre_email'
    MAIL_PASSWORD = 'votre_mot_de_passe'


# Sélectionnez la configuration en fonction de l'environnement (développement, production, etc.)
if os.environ.get('FLASK_ENV') == 'production':
    app_config = Config  # Utilisez la même classe de configuration pour la production
else:
    app_config = Config
