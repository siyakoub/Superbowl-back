import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.odds_service import OddsService

odds_bp = Blueprint("odd", __name__)


@odds_bp.route("/odds", methods=["GET"])
def get_All_Odds_route():
    try:
        odds = OddsService.get_all_service()
        if odds:
            return jsonify(
                {
                    "cotes": [
                        odd.__dict__ for odd in odds
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune côtes n'as été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des côtes...",
                "error": str(e)
            }
        ), 500


@odds_bp.route('/odds/<int:id_odd>', methods=["GET"])
def get_odds_by_id_route(id_odd):
    try:
        odd = OddsService.get_by_id_service(id_odd)
        if odd:
            return jsonify(
                {
                    "cote": odd.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune côtes n'as été trouvé"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération de la côtes...",
                "error": str(e)
            }
        ), 500


@odds_bp.route('/odds/<int:team_id>', methods=["GET"])
def get_odd_by_team_id_route(team_id):
    try:
        odd = OddsService.get_by_team_service(team_id)
        if odd:
            return jsonify(
                {
                    "cote": odd.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucune côte n'a été trouvé pour cette équipe..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération de la côtes...",
                "error": str(e)
            }
        ), 500


@odds_bp.route('/odds', methods=["POST"])
def create_odd_route():
    try:
        data = request.get_json()
        coteVictoire = data["coteVictoire"]
        team_id = data['idTeam']
        OddsService.create_odds_service(coteVictoire, team_id)
        odd = OddsService.get_by_team_service(team_id)
        if odd:
            return jsonify(
                {
                    "message": "côte ajouté avec succès...",
                    "cote": odd.__dict__
                }
            ), 201
        else:
            return jsonify(
                {
                    "errorMessage": "L'ajout de la côte ne s'est pas fait..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de l'ajout de la côte...",
                "error": str(e)
            }
        ), 500


@odds_bp.route('/odds/<int:team_id>', methods=["PUT"])
def update_odd_route(team_id):
    try:
        odd = OddsService.get_by_team_service(team_id)
        data = request.get_json()
        coteVictoire = data["coteVictoire"]
        odd.update(coteVictoire)
        odd = odd.get_by_team(team_id)
        if odd:
            return jsonify(
                {
                    "message": "Côte mise à jour avec succès !",
                    "cote": odd.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "La mise à jour n'est pas été un succès..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la mise à jour de la côte...",
                "error": str(e)
            }
        ), 500


@odds_bp.route('/odds/<int:team_id>', methods=["DELETE"])
def delete_odd_route(team_id):
    try:
        odd = OddsService.get_by_team_service(team_id)
        odd.delete_odds()
        newOdd = OddsService.get_by_team_service(team_id)
        if newOdd is None:
            return jsonify(
                {
                    "message": "Côtes supprimé avec succès..."
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Côtes non supprimé...Réessayé.."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la suppression de la côtes",
                "error": str(e)
            }
        ), 500







