import time
import urllib.parse
from flask import Blueprint, request, jsonify
from app.utils.hashFunction import hash_password
from app.services.bet_service import BetService
from app.services.user_service import UserService
from app.services.team_service import TeamService
from app.services.match_service import MatchService
from app.services.odds_service import OddsService

bet_bp = Blueprint("bet", __name__)

@bet_bp.route("/bets", methods=["GET"])
def get_all_bet_route():
    try:
        bets = BetService.get_all_bet_service()
        if bets:
            return jsonify(
                {
                    "Paris": [
                        bet.__dict__ for bet in bets
                    ]
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun paris n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupérations des paris...",
                "error": str(e)
            }
        ), 500

@bet_bp.route("/bets/<int:bet_id>", methods=["GET"])
def get_bet_by_id_route(bet_id):
    try:
        bet = BetService.get_bet_by_id_service(bet_id)
        if bet:
            return jsonify(
                {
                    "Pari": bet.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun pari n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération du pari...",
                "error": str(e)
            }
        ), 500

@bet_bp.route("/bets/<int:team_id>/byteam", methods=["GET"])
def get_all_bet_by_team_id(team_id):
    try:
        bets = BetService.get_bet_all_by_team_id_service(team_id)
        team = TeamService.get_team_by_id_service(team_id)
        if bets and team:
            return jsonify(
                {
                    "Paris": [
                        bet.__dict__ for bet in bets
                    ],
                    "Team": team.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun paris n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des paris...",
                "error": str(e)
            }
        ), 500

@bet_bp.route("/bets/<int:match_id>/bymatch", methods=["GET"])
def get_all_bet_by_match(match_id):
    try:
        bets = BetService.get_bet_all_by_match_id_service(match_id)
        match = MatchService.get_match_by_id_service(match_id)
        if bets and match:
            return jsonify(
                {
                    "Paris": [
                        bet.__dict__ for bet in bets
                    ],
                    "Match": match.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun paris n'a été trouvé pour ce match..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des paris...",
                "error": str(e)
            }
        ), 500


@bet_bp.route("/bets/<int:user_id>/byuser", methods=["GET"])
def get_all_bet_by_user_id_route(user_id):
    try:
        bets = BetService.get_all_bet_by_user_id_service(user_id)
        user = UserService.get_user_by_id_service(user_id)
        if bets and user:
            return jsonify(
                {
                    "Paris": [
                        bet.__dict__ for bet in bets
                    ],
                    "Utilisateur": user.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun paris trouvé pour cette utilisateur..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la récupération des paris de l'utilisateur...",
                "error": str(
                    e
                )
            }
        ), 500


@bet_bp.route("/bets", methods=["POST"])
def create_bet_route():
    try:
        data = request.get_json()
        team_domicile = data["teamDomicile"]
        team_exterieur = data["teamExterieur"]
        team = data["team"]
        userID = data["userID"]
        montant_miser = data["montantMiser"]
        team_Domicile = TeamService.get_team_by_name_service(team_domicile)
        team_Exterieur = TeamService.get_team_by_name_service(team_exterieur)
        teamchoisi = TeamService.get_team_by_name_service(team)
        user = UserService.get_user_by_id_service(userID)
        match = MatchService.get_match_by_teams_service(team_Domicile.teamID, team_Exterieur.teamID)
        oddTeam = OddsService.get_by_team_service(teamchoisi.teamID)
        montant_potentiel = oddTeam.coteVictoire * montant_miser
        BetService.create_bet_service(user.userID, match.matchID, teamchoisi, montant_miser, montant_potentiel)
        bets = BetService.get_all_bet_by_user_id_service(user.userID)
        if bets:
            return jsonify(
                {
                    "message": "Le pari à été ajouté !",
                    "Paris": [
                        bet.__dict__ for bet in bets
                    ]
                }
            ), 201
        else:
            return jsonify(
                {
                    "errorMessage": "Le pari n'a pas été ajouté..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la création du pari...",
                "error": str(e)
            }
        ), 500

@bet_bp.route("/bets/<int:bet_id>", methods=["PUT"])
def update_bet_route(bet_id):
    try:
        data = request.get_json()
        team_domicile = data["teamDomicile"]
        team_exterieur = data["teamExterieur"]
        team = data["team"]
        userID = data["userID"]
        montant_miser = data["montantMiser"]
        user = UserService.get_user_by_id_service(userID)
        teamChoisi = TeamService.get_team_by_name_service(team)
        teamDomicile = TeamService.get_team_by_name_service(team_domicile)
        teamExterieur = TeamService.get_team_by_name_service(team_exterieur)
        match = MatchService.get_match_by_teams_service(teamDomicile.teamID, teamExterieur.teamID)
        odds = OddsService.get_by_team_service(teamChoisi.teamID)
        montant_potentiel = odds.coteVictoire * montant_miser
        bet = BetService.get_bet_by_id_service(bet_id)
        bet.update(user.userID, match.matchID, teamChoisi.teamID, montant_miser, montant_potentiel)
        bet = bet.get_by_id(bet_id)
        if bet and bet.montantPotentiel == montant_potentiel:
            return jsonify(
                {
                    "message": "La mise à jour du pari à été effectuer...",
                    "Pari": bet.__dict__
                }
            ), 200
        else:
            return jsonify(
                {
                    "errorMessage": "La mise à jour n'a pas été effectué..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la mise à jour du pari...",
                "error": str(e)
            }
        ), 500


@bet_bp.route("/bets/<int:bet_id>", methods=["DELETE"])
def delete_bet_route(bet_id):
    try:
        bet = BetService.get_bet_by_id_service(bet_id)
        if bet:
            bet.delete()
            bet = bet.get_by_id(bet_id)
            if bet is None:
                return jsonify(
                    {
                        "message": "Le pari à été supprimé correctement..."
                    }
                ), 200
            else:
                return jsonify(
                    {
                        "errorMessage": "Le pari n'a pas été supprimé correctement"
                    }
                ), 404
        else:
            return jsonify(
                {
                    "errorMessage": "Aucun pari n'a été trouvé..."
                }
            ), 404
    except Exception as e:
        return jsonify(
            {
                "errorMessage": "Une erreur est survenue lors de la suppression du paris...",
                "error": str(e)
            }
        ), 500







