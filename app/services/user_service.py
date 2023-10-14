from app import mysql
from app.models.user import User


class UserService:
    @staticmethod
    def create_user_service(nom, prenom, adresseEmail, motDePasse):
        user = User(nom, prenom, adresseEmail, motDePasse)
        user.save()

    @staticmethod
    def get_user_by_email_actif_service(email):
        return User.get_by_email_actif(email)

    @staticmethod
    def get_user_by_email_inactif_service(email):
        return User.get_by_email_inactif(email)

    @staticmethod
    def get_user_by_email_service(email):
        return User.get_by_email(email)

    @staticmethod
    def get_all_users_actif_service():
        return User.get_all_users_actif()

    @staticmethod
    def get_all_users_inactif_service():
        return User.get_all_users_inactif()

    @staticmethod
    def get_all_users_service():
        return User.get_all_users()

    @staticmethod
    def get_user_by_id_service(id):
        return User.get_by_id(id)

    @staticmethod
    def update_user_service(nom, prenom, adresseEmail, motDePasse, emailBase):
        return User.update_user(nom, prenom, adresseEmail, motDePasse, emailBase)

    @staticmethod
    def delete_user_service(user):
        user.delete_user()


    @staticmethod
    def desactivate_user_service(user):
        user.desactivate_user()
