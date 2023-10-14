import datetime
import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.session_service import SessionService
from app.services.user_service import UserService

session_bp = Blueprint("session", __name__)

@session_bp.route("/sessions", methods=["GET"])
def get_all_sessions_route():
    try:
        sessions = SessionService.get_all_session()
        if sessions:
            return jsonify(
                {
                    "sessions": [
                        session.__dict__ for session in sessions
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune session trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des sessions...",
                "error": str(e)
            }
        ), 500

@session_bp.route("/sessions/<int:session_id>", methods=["GET"])
def get_session_by_id_route(session_id):
    try:
        session = SessionService.get_session_by_id_service(session_id)
        if session:
            return jsonify(
                {
                    "Session": session.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune équipe n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de lma récupération de la session...",
                "error": str(e)
            }
        ), 500

@session_bp.route("/session/<string:email>", methods=["GET"])
def get_all_sessions_by_userID(email):
    try:
        emailDecoded = urllib.parse.unquote(email, "UTF-8")
        sessions = SessionService.get_all_session_by_email(emailDecoded)
        user = UserService.get_user_by_email_service(emailDecoded)
        if sessions and user:
            return jsonify(
                {
                    "Sessions": [
                        session.__dict__ for session in sessions
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune sessions trouvé pour l'utilisateur..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des sessions utilisateur...",
                "error": str(e)
            }
        ), 500

@session_bp.route("/sessions", methods=["POST"])
def create_session_route():
    try:
        data = request.get_json()
        email = data["emailUser"]
        dateHeureDebut = datetime.datetime.now()
        dateHeureFin = dateHeureDebut + datetime.timedelta(hours=24)
        SessionService.create_session_service(email, dateHeureDebut, dateHeureFin)
        return jsonify(
            {
                "message": "L'ajout de la session à bien été effectué..."
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la création de la session...",
                "error": str(e)
            }
        ), 500


@session_bp.route("/session", methods=["GET"])
def get_session_by_token_route():
    try:
        token = request.headers.get("token")
        session = SessionService.get_session_by_token_service(token)
        if session:
            return jsonify(
                {
                    "Session": session.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune session n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération de la session...",
                "error": str(e)
            }
        ), 500


@session_bp.route("/sessions/<int:session_id>", methods=["DELETE"])
def delete_session_route(session_id):
    try:
        session = SessionService.get_session_by_id_service(session_id)
        if session:
            session.delete()
            session = SessionService.get_session_by_id_service(session_id)
            if session is None:
                return jsonify(
                    {
                        "message": "La suppression de la session à été effectué avec succès !"
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "La suppression n'a pas été effectué avec succès..."
                    }
                ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la suppression de la session...",
                "error": str(e)
            }
        ), 500




