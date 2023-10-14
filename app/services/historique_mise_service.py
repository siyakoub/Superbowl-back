from app.models.historiqueMise import HistoriqueMise


class HistoriqueMiseService:

    @staticmethod
    def create_historiqueMise_service(userID, matchID, montantMiser, resultat):
        historique_mise = HistoriqueMise(userID, matchID, montantMiser, resultat)
        historique_mise.save()

    @staticmethod
    def update_historiqueMise_service(historiqueID, userID, matchID, montantMiser, resultat):
        historique_mise = HistoriqueMise.get_by_id(historiqueID)
        if historique_mise:
            historique_mise.update(userID, matchID, montantMiser, resultat)
        else:
            pass

    @staticmethod
    def delete_historiqueMise_service(historiqueID):
        historique_mise = HistoriqueMise.get_by_id(historiqueID)
        if historique_mise:
            historique_mise.delete()
        else:
            pass

    @staticmethod
    def get_all_historiqueMise():
        return HistoriqueMise.get_all()

    @staticmethod
    def get_all_by_userID_service(user_id):
        return HistoriqueMise.get_all_by_user_id(user_id)

    @staticmethod
    def get_all_historiqueMise_by_match_service(match_id):
        return HistoriqueMise.get_all_by_metch_id(match_id)

    @staticmethod
    def get_historique_mise_by_id_service(historique_mise_id):
        return HistoriqueMise.get_by_id(historique_mise_id)
