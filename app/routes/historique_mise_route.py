import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.bet_service import BetService
from app.services.historique_mise_service import HistoriqueMiseService
from app.services.user_service import UserService
from app.services.match_service import MatchService
from app.services.team_service import TeamService


historique_mise_bp = Blueprint("historiquemise", __name__)


@historique_mise_bp.route("/historiquesmises", methods=["GET"])
def get_all_historiques_mises_route():
    try:
        historiques_mises = HistoriqueMiseService.get_all_historiqueMise()
        if historiques_mises:
            return jsonify(
                {
                    "historiquesMises": historique_mise.__dict__ for historique_mise in historiques_mises
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune historiques de mise n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des historiques de mises...",
                "error": str(e)
            }
        ), 500


@historique_mise_bp.route("/historiquesmises/<int:historique_id>", methods=["GET"])
def get_historique_mise_by_id_route(historique_id):
    try:
        historique_mise = HistoriqueMiseService.get_historique_mise_by_id_service(historique_id)
        if historique_mise:
            return jsonify(
                {
                    "historiqueMise": historique_mise.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune historique de mise n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération de l'historique de la mise...",
                "error": str(e)
            }
        ), 500


@historique_mise_bp.route("/historiquesmises/<int:user_id>/byuser", methods=["GET"])
def get_all_historiques_msies_by_user_id_route(user_id):
    try:
        historiques_mises = HistoriqueMiseService.get_all_by_userID_service(user_id)
        user = UserService.get_user_by_id_service(user_id)
        if historiques_mises and user:
            return jsonify(
                {
                    "historiqueMises": [
                        historique_mise.__dict__ for historique_mise in historiques_mises
                    ],
                    "utilisateur": user.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune historique de mise n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des historiques de mises...",
                "error": str(e)
            }
        ), 500


@historique_mise_bp.route("/historiquesmises/<int:match_id>/bymatch", methods=["GET"])
def get_historiques_mises_by_match_id_route(match_id):
    try:
        historiques_mises = HistoriqueMiseService.get_all_historiqueMise_by_match_service(match_id)
        match = MatchService.get_match_by_id_service(match_id)
        if historiques_mises and match:
            return jsonify(
                {
                    "historiqueMises": [
                        historique_mise.__dict__ for historique_mise in historiques_mises
                    ],
                    "match": match.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune historique de mise n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des historique de mises du match...",
                "error": str(e)
            }
        ), 500


@historique_mise_bp.route("/historiquesmises", methods=["POST"])
def create_historique_mise_route():
    try:
        data = request.get_json()
        useremail = data["userEmail"]
        teamDomicile = data["teamDomicile"]
        teamExterieur = data["teamExterieur"]
        montantMiser = data["montantMiser"]
        resultat = data["resultat"]
        user = UserService.get_user_by_email_service(useremail)
        team1 = TeamService.get_team_by_name_service(teamDomicile)
        team2 = TeamService.get_team_by_name_service(teamExterieur)
        match = MatchService.get_match_by_teams_service(team1.teamID, team2.teamID)
        HistoriqueMiseService.create_historiqueMise_service(user.userID, match.matchID, montantMiser, resultat)
        historiqueMises = HistoriqueMiseService.get_all_historiqueMise_by_match_service(match.matchID)
        if historiqueMises:
            return jsonify(
                {
                    "message": "Création de l'historique réussi !",
                    "HistoriquesMises": [
                        historiqueMise.__dict__ for historiqueMise in historiqueMises
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "La mise à jour n'a pas été effectif..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est suvenue lors de la création de l'historique de mise...",
                "error": str(e)
            }
        ), 500

@historique_mise_bp.route("/historiquesmises/<int:historique_mise_id>", methods=["PUT"])
def update_route(historique_mise_id):
    try:
        data = request.get_json()
        team_domicile = data["teamDomicile"]
        team_exterieur = data["teamExterieur"]
        usermail = data["emailUser"]
        montant_mise = data["montantMiser"]
        resultat = data['resultat']
        historique_mise = HistoriqueMiseService.get_historique_mise_by_id_service(historique_mise_id)
        if historique_mise:
            team1 = TeamService.get_team_by_name_service(team_domicile)
            team2 = TeamService.get_team_by_name_service(team_exterieur)
            match = MatchService.get_match_by_teams_service(team1.teamID, team2.teamID)
            user = UserService.get_user_by_email_service(usermail)
            historique_mise.update(user.userID, match.matchID, montant_mise, resultat)
            historique_mise = historique_mise.get_by_id(historique_mise_id)
            if historique_mise:
                return jsonify(
                    {
                        "message": "La mise à jour à été fait correctement...",
                        "historiqueMise": historique_mise.__dict__
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "La mise à jour n'a pas été effectué correctement..."
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune historique avec cette id n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la mise à jour de l'historique de mise...",
                "error": str(e)
            }
        ), 500


@historique_mise_bp.route("/historiquesmises/<int:historique_mise_id>", methods=["DELETE"])
def delete_historique_route(historique_mise_id):
    try:
        historique_mise = HistoriqueMiseService.get_historique_mise_by_id_service(historique_mise_id)
        if historique_mise:
            historique_mise.delete()
            historique_mise = historique_mise.get_by_id(historique_mise_id)
            if historique_mise is None:
                return jsonify(
                    {
                        "message": "La suppression à été effectué avec succès !"
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "La suppression n'a pas été effectué avec succès !",
                        "historiqueMise": historique_mise.__dict__
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune historique de mise n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la suppression de l'historique de mise...",
                "error": str(e)
            }
        ), 500










