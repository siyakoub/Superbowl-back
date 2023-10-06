import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.team_service import TeamService
from app.services.player_service import PlayerService

player_bp = Blueprint("player", __name__)


@player_bp.route("/players", methods=["GET"])
def get_all_player_route():
    try:
        players = PlayerService.get_all_player_service()
        if players:
            return jsonify(
                [
                    player.__dict__ for player in players
                ]
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun joueur n'a été trouver..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération des joueurs",
                "Error": str(e)
            }
        ), 500


@player_bp.route("/players/<int:player_id>", methods=["GET"])
def get_player_by_id_route(player_id):
    try:
        player = PlayerService.get_player_by_id_service(player_id)
        team = TeamService.get_team_by_id_service(player.team_ID)
        if player and team:
            return jsonify(
                {
                    "player": player.__dict__,
                    "team": team.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun joueur avec l'id " + player_id + " trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération du joueur...",
                "Error": str(e)
            }
        ), 500


@player_bp.route("/players/search", methods=["GET"])
def get_player_by_name_complete_route():
    try:
        data = request.get_json()
        name = data["name"]
        firstName = data["firstName"]
        player = PlayerService.get_player_by_name_complete_service(name, firstName)
        team = TeamService.get_team_by_id_service(player.team_ID)
        if player and team:
            return jsonify(
                {
                    "player": player.__dict__,
                    "team": team.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun joueur avec le nom " + firstName + " trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la récupération du joueur...",
                "Error": str(e)
            }
        ), 500


@player_bp.route("/players", methods=["POST"])
def create_player_route():
    try:
        data = request.get_json()
        player_name = data["name"]
        player_firstName = data["firstName"]
        player_number = data["number"]
        team_name = data["teamName"]
        team = TeamService.get_team_by_name_service(team_name)
        print(team.name)
        PlayerService.create_player_service(player_name, player_firstName, player_number, team.teamID)
        player = PlayerService.get_player_by_name_complete_service(player_name, player_firstName)
        print(player)
        if player:
            return jsonify(
                {
                    "player": player.__dict__,
                    "team": team.__dict__
                }
            ), 201
        else:
            return jsonify(
                {
                    "ErrorMessage": "Equipe non trouvé"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de l'ajout du joueur",
                "Error": str(e)
            }
        ), 500


@player_bp.route("/players", methods=["PUT"])
def update_player_route():
    try:
        data = request.get_json()
        player_name = data["name"]
        player_firstName = data["firstName"]
        new_player_name = data["newName"]
        new_player_firstName = data["newFirstName"]
        player_number = data["number"]
        team_name = data["teamName"]
        team = TeamService.get_team_by_name_service(team_name)
        player = PlayerService.get_player_by_name_complete_service(player_name, player_firstName)
        player.update_player(new_player_name, new_player_firstName, player_number, team.teamID)
        newplayer = player.get_player_by_name_complete(new_player_name, new_player_firstName)
        if newplayer:
            return jsonify(
                {
                    "player": newplayer.__dict__,
                    "team": team.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "message": "Aucun joueur trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la mise à jour du joueur...",
                "Error": str(e)
            }
        ), 500


@player_bp.route("/players", methods=["DELETE"])
def delete_player_route():
    try:
        data = request.get_json()
        player_name = data["name"]
        player_firstName = data["firstName"]
        PlayerService.delete_player_service(player_name, player_firstName)
        deleted = PlayerService.get_player_by_name_complete_service(player_name, player_firstName)
        if deleted is None:
            return jsonify(
                {
                    "message": "La suppression du joueur à été réussi avec succès !"
                }
            ), 200
        else:
            return jsonify(
                {
                    "ErrorMessage": "Aucun joueur trouvé avec ces paramètres..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "ErrorMessage": "Une erreur est survenue lors de la suppression du joueur",
                "Error": str(e)
            }
        )


