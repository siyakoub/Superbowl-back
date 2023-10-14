from app import mysql


class HistoriqueMise:

    def __init__(self, userID, matchID, montantMiser, resultat, historiqueMiseID=None):
        self.userID = userID
        self.matchID = matchID
        self.montantMiser = montantMiser
        self.resultat = resultat
        self.historiqueMiseID = historiqueMiseID

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createHistoriqueMise(%s, %s, %s, %s)",
            (self.userID, self.matchID, self.montantMiser, self.resultat)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_id(historique_mise_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from HistoriqueMises where historiqueID=%s",
            (historique_mise_id,)
        )
        historique_mise_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if historique_mise_data:
            historique_miseID = historique_mise_data[0]
            userID = historique_mise_data[1]
            matchID = historique_mise_data[2]
            montantMiser = historique_mise_data[3]
            resultat = historique_mise_data[4]
            return HistoriqueMise(userID, matchID, montantMiser, resultat, historique_miseID)
        else:
            return None

    @staticmethod
    def get_all():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from HistoriqueMises"
        )
        historiques_mises_data = cursor.fetchall()
        cursor.close()
        conn.close()
        historiques_mises = []
        if historiques_mises_data:
            for historique_mise_data in historiques_mises_data:
                historique_miseID = historique_mise_data[0]
                userID = historique_mise_data[1]
                matchID = historique_mise_data[2]
                montantMiser = historique_mise_data[3]
                resultat = historique_mise_data[4]
                historiques_mises.append(
                    HistoriqueMise(userID, matchID, montantMiser, resultat, historique_miseID)
                )
            return historiques_mises
        else:
            return None

    @staticmethod
    def get_all_by_user_id(userID):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from HistoriqueMises where userID=%s",
            (userID,)
        )
        historiques_mises_data = cursor.fetchall()
        cursor.close()
        conn.close()
        historiques_mises = []
        if historiques_mises_data:
            for historique_mise_data in historiques_mises_data:
                historique_miseID = historique_mise_data[0]
                userID = historique_mise_data[1]
                matchID = historique_mise_data[2]
                montantMiser = historique_mise_data[3]
                resultat = historique_mise_data[4]
                historiques_mises.append(
                    HistoriqueMise(userID, matchID, montantMiser, resultat, historique_miseID)
                )
            return historiques_mises
        else:
            return None

    @staticmethod
    def get_all_by_metch_id(match_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from HistoriqueMises where confrontationID=%s",
            (match_id,)
        )
        historiques_mises_data = cursor.fetchall()
        cursor.close()
        conn.close()
        historiques_mises = []
        if historiques_mises_data:
            for historique_mise_data in historiques_mises_data:
                historique_miseID = historique_mise_data[0]
                userID = historique_mise_data[1]
                matchID = historique_mise_data[2]
                montantMiser = historique_mise_data[3]
                resultat = historique_mise_data[4]
                historiques_mises.append(
                    HistoriqueMise(userID, matchID, montantMiser, resultat, historique_miseID)
                )
            return historiques_mises
        else:
            return None

    def update(self, userID, matchID, montanMiser, resultat):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update HistoriqueMises set userID=%s, confrontationID=%s, montantMise=%s, resultat=%s where historiqueID=%s",
            (userID, matchID, montanMiser, resultat, self.historiqueMiseID)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from HistoriqueMises where historiqueID=%s",
            (self.historiqueMiseID,)
        )
        conn.commit()
        cursor.close()
        conn.close()

