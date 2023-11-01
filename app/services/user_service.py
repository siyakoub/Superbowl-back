from app import mysql
from app.models.user import User
from app.utils.tokenResetPassword import generate_reset_token
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config


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
    def reset_password_service(email, password):
        user = User.get_by_email_actif(email)
        if user:
            user.resetPassword(password)
        else:
            raise Exception("Utilisateur introuvable")

    @staticmethod
    def request_reset_password(email):
        user = User.get_by_email_actif(email)
        if user:
            reset_token = generate_reset_token()

            subject = "Réinitialisation du mot de passe"
            from_email = ""
            to_email = email
            message = MIMEMultipart()
            message["From"] = from_email
            message["To"] = to_email
            message["Subject"] = subject
            body = f"Bonjour {user['name']},\n\nVous pouvez réinitialiser votre mot de passe en cliquant sur ce lien : {reset_token}"
            message.attach(MIMEText(body, "plain"))
            email_text = message.as_string()

            # Envoi de l'email
            try:
                if Config.MAIL_USE_TLS:
                    server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
                    server.starttls()
                    server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
                    server.sendmail(from_email, to_email, email_text)
                    server.quit()
                else:
                    server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
                    server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
                    server.sendmail(from_email, to_email, email_text)
                    server.quit()

                print("L'E-mail de réinistalisation du mot de passe à été envoyé avec succès !")
                return True
            except smtplib.SMTPException as e:
                print(f"Erreur lors de l'envoi de l'e-mail : {str(e)}")
        else:
            print("Utilisateur introuvable...")
            return None

    @staticmethod
    def desactivate_user_service(user):
        user.desactivate_user()
