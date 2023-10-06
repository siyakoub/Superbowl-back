from app.models.Odds import Odds


class OddsService:

    @staticmethod
    def create_odds_service(coteVictoire, teamID):
        odds = Odds(teamID, coteVictoire)
        odds.save()

    @staticmethod
    def update_odds_service(teamID, coteVictoire):
        odds = Odds.get_by_team(teamID)
        if odds:
            odds.update(coteVictoire)
        else:
            pass

    @staticmethod
    def delete_odds_service(teamId):
        odds = Odds.get_by_team(teamId)
        if odds:
            odds.delete_odds()
        else:
            pass

    @staticmethod
    def get_by_id_service(coteId):
        return Odds.get_by_id(coteId)

    @staticmethod
    def get_by_team_service(team_id):
        return Odds.get_by_team(team_id)

    @staticmethod
    def get_all_service():
        return Odds.get_all()
