import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.match_service import MatchService
from app.services.team_service import TeamService

match_bp = Blueprint("match", __name__)


@match_bp.route("/matchs", methods=["GET"])
def get_all_match_route():
    try:
        matchs = MatchService.get_all_match_service()
        if matchs:
            return jsonify(
                {
                    "matchs": [
                        match.__dict__ for match in matchs
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun match trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des matchs",
                "error": str(e)
            }
        ), 500


@match_bp.route("/matchs/<int:match_id>", methods=["GET"])
def get_match_by_id_route(match_id):
    try:
        match = MatchService.get_match_by_id_service(match_id)
        if match:
            return jsonify(
                {
                    "match": match.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun match n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération du match...",
                "error": str(e)
            }
        ), 500


@match_bp.route("/matchs/byteams", methods=["GET"])
def get_match_by_teams_route():
    try:
        data = request.get_json()
        equipeDomicile = data["team_domicile"]
        equipeExterieur = data["team_exterieur"]
        teamDomicile = TeamService.get_team_by_name_service(equipeDomicile)
        teamExterieur = TeamService.get_team_by_name_service(equipeExterieur)
        match = MatchService.get_match_by_teams_service(teamDomicile.teamID, teamExterieur.teamID)
        if match:
            return jsonify(
                {
                    "match": match.__dict__
                }
            ), 200
        else:
            return jsonify({
                "errorMessage": "Aucun match n'as été trouvé..."
            }), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération du match...",
                "error": str(e)
            }
        ), 500


@match_bp.route("/matchs/<int:id_match>/start")
def startMatch(id_match):
    try:
        MatchService.start_match_service(id_match)
        time.sleep(1)
        match = MatchService.get_match_by_id_service(id_match)
        if match and match.statut == "EnCours":
            return jsonify(
                {
                    "message": "Le match à démarrer !",
                    "match": match.__dict__
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
                "errorMessage": "Une erreur est survenue lors du lancement du match...",
                "error": str(e)
            }
        ), 500


@match_bp.route("/matchs/<int:id_match>/end")
def end_match_route(id_match):
    try:
        MatchService.end_match_service(id_match)
        time.sleep(1)
        match = MatchService.get_match_by_id_service(id_match)
        if match and match.statut == "Termine":
            return jsonify(
                {
                    "message": "Le match à été fini avec succès...",
                    "match": match.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "La fin du match n'as pas été lancé avec succès.."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la mise à jour de la fin du match...",
                "error": str(e)
            }
        ), 500


@match_bp.route("/matchs", methods=["POST"])
def create_match_route():
    try:
        data = request.get_json()
        teamDomicile = data["teamDomicile"]
        teamExterieur = data["teamExterieur"]
        dateDebut = data["dateHeureDebut"]
        dateFin = data["dateHeureFin"]
        statut = data["statut"]

        team1 = TeamService.get_team_by_name_service(teamDomicile)
        team2 = TeamService.get_team_by_name_service(teamExterieur)
        MatchService.create_match_service(dateDebut, dateFin, statut, team1.teamID, team2.teamID)
        match = MatchService.get_match_by_teams_service(team1.teamID, team2.teamID)
        if match:
            return jsonify(
                {
                    "message": "match crée avec succès !",
                    "match": match.__dict__
                }
            ), 201
        else:
            return jsonify(
                {
                    "errorMessage": "L'équipe n'as pas été crée..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la création du match...",
                "error": str(e)
            }
        ), 500


@match_bp.route("/matchs/upcommings")
def get_all_a_venir_route():
    try:
        matchs = MatchService.get_all_a_venir_service()
        if matchs:
            return jsonify(
                {
                    "matchs": [
                        match.__dict__ for match in matchs
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun match à venir trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des matchs à venir...",
                "error": str(e)
            }
        ), 500


@match_bp.route("/matchs/<int:match_id>", methods=["PUT"])
def update_match_route(match_id):
    try:
        data = request.get_json()
        teamDomicile = data["teamDomicile"]
        teamExterieur = data["teamExterieur"]
        statut = data["statut"]
        dateDebut = data["dateHeureDebut"]
        dateFin = data["dateHeureFin"]
        team1 = TeamService.get_team_by_name_service(teamDomicile)
        team2 = TeamService.get_team_by_name_service(teamExterieur)
        matchBase = MatchService.get_match_by_id_service(match_id)
        matchBase.update_match_service(dateDebut, dateFin, statut, team1.teamID, team2.teamID)
        match = MatchService.get_match_by_teams_service(team1.teamID, team2.teamID)
        if match:
            return jsonify(
                {
                    "message": "Match mis à jour avec succès !",
                    "match": match.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "eroorMessage": "La mise à jour n'as pas été effective..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la mise à jour du match",
                "error": str(e)
            }
        ), 500


@match_bp.route("/matchs/<int:match_id>", methods=["DELETE"])
def delete_match_route(match_id):
    try:
        matchBase = MatchService.get_match_by_id_service(match_id)
        matchBase.delete()
        match = MatchService.get_match_by_id_service(match_id)
        if match is None:
            return jsonify(
                {
                    "message": "Le match à été supprimé avec succès...",
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Le match n'a pas été supprimé correctement..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la suppression du match...",
                "error": str(e)
            }
        ), 500



