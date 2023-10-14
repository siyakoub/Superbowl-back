import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.comment_service import CommentService
from app.services.match_service import MatchService
from app.services.team_service import TeamService
import datetime

comment_bp = Blueprint("comment", __name__)

@comment_bp.route("/comments", methods=["GET"])
def get_all_comment_route():
    try:
        comments = CommentService.get_all_comment_service()
        if comments:
            return jsonify(
                {
                    "comments": [
                        comment.__dict__ for comment in comments
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun commentaire n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des commentaires...",
                "error": str(e)
            }
        ), 500

@comment_bp.route("/comments/<int:comment_id>", methods=["GET"])
def get_comment_by_id_route(comment_id):
    try:
        comment = CommentService.get_comment_by_id_service(comment_id)
        if comment:
            return jsonify(
                {
                    "commentaire": comment.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun commentaire n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération du commentaire...",
                "error": str(e)
            }
        ), 500


@comment_bp.route("/comments/bymatch/<int:match_id>", methods=["GET"])
def get_comment_by_match_id_route(match_id):
    try:
        comments = CommentService.get_all_comment_by_match_id_service(match_id)
        if comments:
            return jsonify(
                {
                    "commentaires": [
                        comment.__dict__ for comment in comments
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun commentaire n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des commentaire du match...",
                "error": str(e)
            }
        ), 500

@comment_bp.route("/comments", methods=["POST"])
def create_comment_route():
    try:
        data = request.get_json()
        teamDomicile = data["teamDomicile"]
        teamExterieur = data["teamExterieur"]
        commentateur = data["commentateur"]
        text = data["commentaire"]
        datNow = str(datetime.datetime.now())
        team1 = TeamService.get_team_by_name_service(teamDomicile)
        team2 = TeamService.get_team_by_name_service(teamExterieur)
        match = MatchService.get_match_by_teams_service(team1.teamID, team2.teamID)
        CommentService.create_comment_service(match.matchID, commentateur, text, datNow)
        comments = CommentService.get_all_comment_by_match_id_service(match.matchID)
        if comments:
            return jsonify(
                {
                    "message": "Le commentaire à été créé avec succès !",
                    "commentaire": [
                        comment.__dict__ for comment in comments
                    ]
                }
            ), 201
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun commentaire n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la création du commentaire...",
                "error": str(e)
            }
        ), 500

@comment_bp.route("/comments/<int:comment_id>", methods=["PUT"])
def update_comment_route(comment_id):
    try:
        comment = CommentService.get_comment_by_id_service(comment_id)
        data = request.get_json()
        match_id = data["matchID"]
        commentateur = data["commentateur"]
        text = data["commentaire"]
        comment.update_comment(match_id, commentateur, text)
        comment = comment.get_by_id(comment_id)
        if comment and comment.commentaire == text and comment.commentateur == commentateur:
            return jsonify(
                {
                    "message": "La mise à jour à été prise en compte avec succès !",
                    "commentaire": comment.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "La mise à jour du commentaire n'a pas été pris en compte...",
                    "error": str(e)
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la mise à jour du commentaire...",
                "error": str(e)
            }
        ), 500

@comment_bp.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment_route(comment_id):
    try:
        comment = CommentService.get_comment_by_id_service(comment_id)
        comment.delete_comment()
        comment = comment.get_by_id(comment_id)
        if comment is None:
            return jsonify(
                {
                    "message": "La suppression du commentaire est un succès..."
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "La suppression n'a pas eu lieu..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la suppression du commentaire...",
                "error": str(e)
            }
        ), 500




