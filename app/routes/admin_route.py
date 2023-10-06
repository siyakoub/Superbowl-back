import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.admin_service import AdminService

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admins", methods=["GET"])
def get_all_admins_route():
    try:
        admins = AdminService.get_all_admin()
        if admins:
            return jsonify(
                [
                    admin.__dict__ for admin in admins
                ]
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun administrateur trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération des administrateurs...",
                "Error": str(e)
            }
        ), 500


@admin_bp.route("/admins/ac", methods=["GET"])
def get_all_admins_actif_route():
    try:
        admins = AdminService.get_all_admin_actif()
        if admins:
            return jsonify(
                [
                    admin.__dict__ for admin in admins
                ]
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun administrateur trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération des administrateurs...",
                "Error": str(e)
            }
        ), 500


@admin_bp.route("/admins/noac", methods=["GET"])
def get_all_admins_inactif_route():
    try:
        admins = AdminService.get_all_admin_inactif()
        if admins:
            return jsonify(
                [
                    admin.__dict__ for admin in admins
                ]
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun administrateur trouvé"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération des utilisateurs...",
                "Error": str(e)
            }
        ), 500


@admin_bp.route("/admins/<int:admin_id>", methods=["GET"])
def get_admin_by_id_route(admin_id):
    try:
        admin = AdminService.get_admin_by_id(admin_id)
        if admin:
            return jsonify(admin.__dict__), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun administrateur avec l'id " + admin_id + " n'a été trouvé"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération de l'administrateur...",
                "Error": str(e)
            }
        ), 500


@admin_bp.route("/admins/ac/<string:login>", methods=["GET"])
def get_admin_actif_by_login_route(login):
    try:
        loginDecoded = urllib.parse.unquote(login, "UTF-8")
        admin = AdminService.get_admin_actif_by_login(loginDecoded)
        if admin:
            return jsonify(admin.__dict__), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun administrateur possèdant le login " + login + " n'a été trouvé...",
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération de l'administrateur...",
                "Error": str(e)
            }
        ), 500


@admin_bp.route("/admins/noac/<string:login>", methods=["GET"])
def get_admin_inactif_by_login_route(login):
    try:
        loginDecoded = urllib.parse.unquote(login, "UTF-8")
        admin = AdminService.get_admin_inactif_by_login(loginDecoded)
        if admin:
            return jsonify(
                admin.__dict__
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun utilisateur possèdant le login " + login + " n'a été trouvé...",
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération de l'administrateur...",
                "Error": str(e)
            }
        ), 500


@admin_bp.route("/admins", methods=["POST"])
def create_admin_route():
    try:
        data = request.get_json()
        login = data["login"]
        password = data["pass"]
        nom = data["nom"]
        prenom = data["prenom"]
        created = AdminService.create_admin(login, password, nom, prenom)
        if created:
            return jsonify(
                {
                    "message": "Administrateur créé avec succès !"
                }
            ), 201
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun administrateur n'a pas été crée..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la création du nouvel administrateur...",
                "Error": str(e)
            }
        ), 500


@admin_bp.route("/admins/<string:login>", methods=["PUT"])
def update_admin_route(login):
    try:
        loginDecoded = urllib.parse.unquote(login, "UTF-8")
        data = request.get_json()
        login = data["login"]
        password = data["pass"]
        nom = data["nom"]
        prenom = data["prenom"]
        admin = AdminService.get_admin_by_login(loginDecoded)
        updated = admin.update_admin(login, password, nom, prenom)
        if updated:
            return jsonify(
                {
                    "message": "Administrateur mise à jour avec succès !"
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun administrateur n'a été trouver...",
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la mise à jour de l'administrateur...",
                "Error": str(e)
            }
        ), 500


@admin_bp.route("/admins/<string:login>/del", methods=["DELETE"])
def delete_admin_route(login):
    try:
        loginDecoded = urllib.parse.unquote(login, "UTF-8")
        admin = AdminService.get_admin_by_login(loginDecoded)
        delete = admin.delete_admin()
        if delete:
            return jsonify(
                {
                    "message": "L'administrateur à été supprimer avec succès !"
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun administrateur n'a été trouver..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la suppression de l'administrateur...",
                "Error": str(e)
            }
        ), 500


@admin_bp.route("/admins/<string:login>", methods=["PUT"])
def desactivate_admin_route(login):
    try:
        loginDecoded = urllib.parse.unquote(login, "UTF-8")
        admin = AdminService.get_admin_actif_by_login(loginDecoded)
        desactivate = admin.desactivate_admin(admin)
        if desactivate:
            return jsonify(
                {
                    "message": "L'administrateur à été désactiver avec succès !"
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun administrateur n'as été trouver..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la désactivation de l'administrateur...",
                "Error": str(e)
            }
        )

