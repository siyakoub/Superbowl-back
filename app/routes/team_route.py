import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.team_service import TeamService

team_bp = Blueprint("team", __name__)


@team_bp.route("/teams", methods=["GET"])
def get_all_teams_route():
    try:
        teams = TeamService.get_all_teams()
        if teams:
            return jsonify(
                [
                    team.__dict__ for team in teams
                ]
            ), 200
        else:
            return jsonify(
                {
                    "message": "Aucun équipe n'a été trouvé"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération des équipes",
                "Error": str(e)
            }
        ), 500


@team_bp.route("/teams/<int:team_id>", methods=["GET"])
def get_teams_by_id_route(team_id):
    try:
        team = TeamService.get_team_by_id_service(team_id)
        if team:
            return jsonify(
                team.__dict__
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucune équipe n'a été trouvé"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenu lors de la récupération",
                "Error": str(e)
            }
        ), 500


@team_bp.route("/teams/<string:team_name>", methods=["GET"])
def get_team_by_name_route(team_name):
    try:
        team = TeamService.get_team_by_name_service(team_name)
        if team:
            return jsonify(
                team.__dict__
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucune équipe avec le nom " + team_name + " trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une exception est survenu lors de la récupération de l'équipe...",
                "Error": str(e)
            }
        ), 500


@team_bp.route("/teams", methods=["POST"])
def create_team_route():
    try:
        data = request.get_json()
        name = data["name"]
        country = data["country"]
        TeamService.create_team_service(name, country)
        team = TeamService.get_team_by_name_service(name)
        if team:
            return jsonify(
                {
                    "message": "Equipe créé avec succès !",
                    "team": team.__dict__
                }
            ), 201
        else:
            return jsonify(
                {
                    "ErrorMessage": "La création de l'équipe à échoué..."
                }
            )
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la création de l'équipe...",
                "Error": str(e)
            }
        )


@team_bp.route("/teams/<string:team_name>", methods=["PUT"])
def update_team_route(team_name):
    try:
        team_name_decoded = urllib.parse.unquote(team_name, "UTF-8")
        data = request.get_json()
        new_team_name = data["name"]
        team_country = data["country"]
        team = TeamService.get_team_by_name_service(team_name_decoded)
        team.update_team(new_team_name, team_country)
        newTeam = TeamService.get_team_by_name_service(new_team_name)
        if newTeam:
            return jsonify(
                {
                    "message": "Equipe mise à jour avec succès !",
                    "team": newTeam.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucune équipe n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la mise à jour de l'équipe...",
                "Error": str(e)
            }
        ), 500


@team_bp.route("/teams/<string:name>", methods=["DELETE"])
def delete_team_route(name):
    try:
        nameDecoded = urllib.parse.unquote(name, "UTF-8")
        team = TeamService.get_team_by_name_service(nameDecoded)
        team.delete_team()
        deleted = TeamService.get_team_by_name_service(nameDecoded)
        if deleted is None:
            return jsonify(
                {
                    "message": "Equipe supprimé avec succès !"
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun équipe n'a été trouver..."
                }
            ), 404
    except Exception as e:
        return jsonify({
            "ErrorMessage": "Une erreur est survenue lors de la suppression de l'équipe...",
            "Error": str(e)
        }), 500






