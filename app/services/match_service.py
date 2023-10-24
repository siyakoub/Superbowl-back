from app.models.match import Match


class MatchService:

    @staticmethod
    def get_match_by_id_service(id_match):
        return Match.get_by_id(id_match)

    @staticmethod
    def get_match_by_teams_service(id_teamDomicile, id_teamExterieur):
        return Match.get_match_by_teams(id_teamDomicile, id_teamExterieur)

    @staticmethod
    def get_all_match_service():
        return Match.get_all_match()

    @staticmethod
    def get_all_a_venir_service():
        return Match.getAllAVenir()

    @staticmethod
    def start_match_service(id_match):
        match = Match.get_by_id(id_match)
        if match:
            match.startMatch()
        else:
            pass

    @staticmethod
    def end_match_service(id_match):
        match = Match.get_by_id(id_match)
        if match:
            match.endMatch()
        else:
            pass

    @staticmethod
    def create_match_service(dateHeureDebut, dateHeureFin, statut, teamDomicileID, teamExterieurID):
        match = Match(dateHeureDebut, dateHeureFin, statut, teamDomicileID, teamExterieurID)
        match.save()

    @staticmethod
    def update_match_service(dateHeureDebut, dateHeureFin, statut, teamDomicileID, teamExterieurID, newTeamDomicileID, newTeamExterieurID):
        match = Match.get_match_by_teams(teamDomicileID, teamExterieurID)
        if match:
            match.update(newTeamDomicileID, newTeamExterieurID, dateHeureDebut, dateHeureFin, statut)
        else:
            pass

    @staticmethod
    def endMatch_service(id_match):
        match = Match.get_by_id(id_match)
        if match:
            match.endMatch()
        else:
            pass

    @staticmethod
    def startMatch_service(id_match):
        match = Match.get_by_id(id_match)
        if match:
            match.startMatch()
        else:
            pass

    @staticmethod
    def delete_match_service(id_match):
        match = Match.get_by_id(id_match)
        if match:
            match.delete()
        else:
            pass

