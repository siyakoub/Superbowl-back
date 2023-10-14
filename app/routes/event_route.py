import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.match_service import MatchService
from app.services.event_service import EventService
from app.services.team_service import TeamService

event_bp = Blueprint("event", __name__)

@event_bp.route("/events", methods=["GET"])
def get_all_event():
    try:
        events = EventService.get_all_event_service()
        if events:
            return jsonify(
                {
                    "Evenements": [
                        event.__dict__ for event in events
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun évènement trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des évènements...",
                "error": str(e)
            }
        ), 500

@event_bp.route("/events/<int:eventID>", methods=["GET"])
def get_event_by_id_route(eventID):
    try:
        event = EventService.get_event_by_id(eventID)
        if event:
            return jsonify(
                {
                    "Evenement": event.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun évènement trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération de l'évènement...",
                "error": str(e)
            }
        ), 500

@event_bp.route("/events/<int:match_id>/bymatchs", methods=["GET"])
def get_all_event_by_match_id_route(match_id):
    try:
        events = EventService.get_all_event_by_match_id(match_id)
        if events:
            return jsonify(
                {
                    "Evenements": [
                        event.__dict__ for event in events
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun évènement n'a été trouvé pour ce match..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération de l'évènement...",
                "error": str(e)
            }
        ), 500


@event_bp.route("/events", methods=["POST"])
def create_event_route():
    try:
        data = request.get_json()
        description = data["description"]
        typeEvent = data["typeEvenement"]
        teamDomicile = data["teamDomicile"]
        teamExterieur = data["teamExterieur"]
        team1 = TeamService.get_team_by_name_service(teamDomicile)
        team2 = TeamService.get_team_by_name_service(teamExterieur)
        match = MatchService.get_match_by_teams_service(team1.teamID, team2.teamID)
        EventService.create_event_service(description, typeEvent, match.matchID)
        events = EventService.get_all_event_by_match_id(match.matchID)
        if events:
            for event in events:
                if event.description == description and event.type == typeEvent:
                    return jsonify(
                        {
                            "message": "L'évènement à été ajouté avec succès !",
                            "Evenement": event.__dict__
                        }
                    ), 200
                else:
                    return jsonify(
                        {
                            "errorMessage": "L'évènement n'a pas été ajouté correctement..."
                        }
                    ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "L'évenement n'a pas été ajouté correctement..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la création de l'évènement...",
                "error": str(e)
            }
        ), 500


@event_bp.route("/events/<int:eventID>", methods=["PUT"])
def update_event_route(eventID):
    try:
        data = request.get_json()
        teamDomicile = data["teamDomicile"]
        teamExterieur = data["teamExterieur"]
        description = data["description"]
        typeEvent = data["typeEvent"]
        team1 = TeamService.get_team_by_name_service(teamDomicile)
        team2 = TeamService.get_team_by_name_service(teamExterieur)
        match = MatchService.get_match_by_teams_service(team1.teamID, team2.teamID)
        event = EventService.get_event_by_id(eventID)
        event.update(description, typeEvent, match.matchID)
        event = event.get_by_id(eventID)
        if event and event.description == description:
            return jsonify(
                {
                    "message": "La mise a jour de l'évènement à été effectué avec succès !",
                    "Evenement": event.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "La mise à jour n'a pas été effectué correctement..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la mise à jour de l'évènement...",
                "error": str(e)
            }
        ), 500


@event_bp.route("/events/<int:eventID>", methods=["DELETE"])
def delete_event_route(eventID):
    try:
        event = EventService.get_event_by_id(eventID)
        event.delete()
        event = event.get_by_id(eventID)
        if event is None:
            return jsonify(
                {
                    "message": "Evenement supprimé avec succès !"
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "L'equipe n'a pas été supprimé avec succès !"
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la suppression de l'évènement...",
                "error": str(e)
            }
        ), 500





