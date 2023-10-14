from app.models.session import Session
import secrets


class SessionService:

    @staticmethod
    def create_session_service(email, dateHeureDebut, dateHeureFin):
        tokencreate = secrets.token_urlsafe(32)
        session = Session(email, tokencreate, dateHeureDebut, dateHeureFin)
        session.save()

    @staticmethod
    def delete_session_service(session_id):
        session = Session.get_by_id(session_id)
        if session:
            session.delete()
        else:
            pass

    @staticmethod
    def get_session_by_id_service(session_id):
        return Session.get_by_id(session_id)

    @staticmethod
    def get_all_session_by_email(email):
        return Session.get_all_by_email(email)

    @staticmethod
    def get_all_session():
        return Session.get_all()

    @staticmethod
    def get_session_by_token_service(token):
        return Session.get_by_token(token)