import datetime
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.user_service import UserService
from app.services.session_service import SessionService

user_bp = Blueprint("user", __name__)


@user_bp.route("/users", methods=["GET"])
def get_all_users_route():
    try:
        users = UserService.get_all_users_service()
        if users:
            return jsonify([user.__dict__ for user in users]), 200
        else:
            return jsonify({"ErrorMessage": "Aucun Utilisateur trouvé"}), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération des utilisateurs...",
                "Error": str(e)
            }
        ), 500


@user_bp.route("/users/ac", methods=["GET"])
def get_all_users_actif_route():
    try:
        users = UserService.get_all_users_actif_service()
        if users:
            return jsonify([user.__dict__ for user in users]), 200
        else:
            return jsonify({"ErrorMessage": "Aucun Utilisateur trouvé"}), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération des utilisateurs...",
                "Error": str(e)
            }
        ), 500


@user_bp.route("users/noac", methods=["GET"])
def get_all_users_inactif_route():
    try:
        users = UserService.get_all_users_inactif_service()
        if users:
            return jsonify([user.__dict__ for user in users]), 200
        else:
            return jsonify({"ErrorMessage" : "Aucun Utilisateur trouvé"}), 200
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération des utilisateurs...",
                "Error": str(e)
            }
        ), 500


@user_bp.route("users/login", methods=["POST"])
def login_route():
    try:
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        user = UserService.get_user_by_email_service(email)
        if user and user.motDePasse == hash_password(password):
            SessionService.create_session_service(email, datetime.datetime.now(), (datetime.datetime.now() + datetime.timedelta(hours=24)))
            sessions = SessionService.get_all_session_by_email(email)
            for session in sessions:
                if session.dateHeureDebut == datetime.datetime.now():
                    return jsonify(
                        {
                            "connected": True,
                            "utilisateur": user.__dict__,
                            "session": session.__dict__
                        }
                    ), 201
                else:
                    pass
        else:
            return jsonify(
                {
                    "connected": False,
                    "erroeMessage": "L'email ou le mot de passe ne correspond à un utilisateur dans la base de données..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la connexion  de l'utilisateur...",
                "error": str(e)
            }
        ), 500


@user_bp.route("/users/logout", methods=["DELETE"])
def logout_route():
    try:
        token = request.headers.get("token")
        session = SessionService.get_session_by_token_service(token)
        if session:
            user = UserService.get_user_by_email_service(session.email)
            if user:
                return jsonify(
                    {
                        "deconnected": True,
                        "session": session.__dict__,
                        "utilisateur": user.__dict__
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "Aucune utilisateur ne possèdent cette session..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune session n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la deconnexion de la session...",
                "error": str(e)
            }
        ), 500



@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id_route(user_id: int):
    try:
        user = UserService.get_user_by_id_service(user_id)
        if user:
            return jsonify(
                {
                    "user": user.__dict__
                }
            ), 200
        else:
            return jsonify({"ErrorMessage": "Aucun Utilisateur avec l'id "+ user_id + " trouvé"})
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération de l'utilisateur...",
                "Error": str(e)
            }
        ), 500


@user_bp.route("/users/<string:email>", methods= ["GET"])
def get_user_by_email_actif_route(email: str):
    try:
        emailDecoded = urllib.parse.unquote(email, "UTF-8")
        user = UserService.get_user_by_email_actif_service(emailDecoded)
        if user:
            return jsonify(
                {
                    "user": user.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun Utilisateur avec l'email " + emailDecoded + " trouvé"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération de l'utilisateur...",
                "Error": str(e)
            }
        ), 500


@user_bp.route("/users", methods=["POST"])
def create_user_route():
    try:
        data = request.get_json()
        nom = data["nom"]
        prenom = data["prenom"]
        email = data["adresseEmail"]
        password = data["motDePasse"]
        password_hashed = hash_password(password)
        UserService.create_user_service(nom, prenom, email, password_hashed)
        user = UserService.get_user_by_email_service(email)
        if user:
            return jsonify({"message": "Utilisateur créé avec succès !",
                            "user": user.__dict__}), 201
        else:
            return jsonify(
                {
                    "ErrorMessage": "L'utilisateur n'as pas été créer"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la création de l'utilisateur...",
                "Error": str(e)
            }
        ), 500


@user_bp.route("/users/<string:email>", methods=["PUT"])
def update_user_route(email):
    try:
        emailDecoded = urllib.parse.unquote(email, "UTF-8")
        data = request.get_json()
        nom = data["nom"]
        prenom = data["prenom"]
        newEmail = data["adresseEmail"]
        password = data["motDePasse"]
        user = UserService.get_user_by_email_actif_service(emailDecoded)
        password_hashed = hash_password(password)
        UserService.update_user_service(nom, prenom, newEmail, password_hashed, emailDecoded)
        newUser = UserService.get_user_by_email_service(newEmail)
        if newUser:
            return jsonify({"message": "Utilisateur mis à jour avec succès !",
                            "user": newUser.__dict__}), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "L'utilisateur n'as pas été créé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la mise à jour de l'utilisateur...",
                "Error": str(e)
            }
        ), 500


@user_bp.route("/users/<string:email>", methods=["DELETE"])
def delete_user_route(email):
    try:
        emailDecoded = urllib.parse.unquote(email, "UTF-8")
        user = UserService.get_user_by_email_service(emailDecoded)
        user.delete_user()
        deleted = UserService.get_user_by_email_service(emailDecoded)
        if deleted:
            return jsonify(
                {
                    "message": "Utilisateur supprimé avec succès !"
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun utilisateur n'as été trouver..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la suppression de l'utilisateur...",
                "Error": str(e)
            }
        ), 500


@user_bp.route("/users/<string:email>/del", methods=["PUT"])
def desactivate_user_route(email):
    try:
        emailDecoded = urllib.parse.unquote(email, "UTF-8")
        user = UserService.get_user_by_email_service(emailDecoded)
        user.desactivate_user()
        desactivate = UserService.get_user_by_email_inactif_service(emailDecoded)
        if desactivate:
            return jsonify(
                {
                    "message": "L'utilisateur à été désactivé avec succès",
                    "userDesactivate": desactivate.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun utilisateur n'as été trouver..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la désactivation de l'utilisateur...",
                "Error": str(e)
            }
        ), 500











