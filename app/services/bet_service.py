from app.models.Bet import Bet

class BetService:

    @staticmethod
    def get_bet_by_id_service(bet_id):
        return Bet.get_by_id(bet_id)

    @staticmethod
    def get_all_bet_by_user_id_service(user_id):
        return Bet.get_all_by_user_id(user_id)

    @staticmethod
    def get_bet_all_by_team_id_service(team_id):
        return Bet.get_all_by_team_id(team_id)

    @staticmethod
    def get_bet_all_by_match_id_service(match_id):
        return Bet.get_all_by_match_id(match_id)

    @staticmethod
    def get_all_bet_service():
        return Bet.get_all()

    @staticmethod
    def create_bet_service(user_id, match_id, team_id, montant_miser, montant_potentiel):
        bet = Bet(user_id, match_id, team_id, montant_miser, montant_potentiel)
        bet.save()

    @staticmethod
    def update_bet_service(bet_id, match_id, team_id, montant_miser, montantPotentiel):
        bet = Bet.get_by_id(bet_id)
        if bet:
            bet.update(match_id, team_id, montant_miser, montantPotentiel)
        else:
            pass

    @staticmethod
    def delete_bet_service(bet_id):
        bet = Bet.get_by_id(bet_id)
        if bet:
            bet.delete()
        else:
            pass


