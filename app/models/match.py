from app import mysql

class Match:

    def __init__(self, dateHeureDebut, dateHeureFin, statut, teamDomicileID, teamExterieurID, matchID=None):
        self.dateHeureDebut = dateHeureDebut
        self.datHeureFin = dateHeureFin
        self.statut = statut
        self.teamDomicileID = teamDomicileID
        self.teamExterieurID = teamExterieurID
        self.matchID = matchID

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createMatch(%s, %s, %s, %s, %s)",
            (self.teamDomicileID, self.teamExterieurID, self.dateHeureDebut, self.datHeureFin, self.statut)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_id(id_confrontation):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from confrontation where confrontationID=%s",
            (id_confrontation,)
        )
        match_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if match_data:
            confrontation_id = match_data[0]
            teamDomicile_id = match_data[1]
            teamExterieur_id = match_data[2]
            dateHeureDebut = match_data[3]
            dateHeureFin = match_data[4]
            statut = match_data[5]
            return Match(dateHeureDebut, dateHeureFin, statut, teamDomicile_id, teamExterieur_id, confrontation_id)
        else:
            return None

    @staticmethod
    def get_all_match():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from confrontation"
        )
        matchs_data = cursor.fetchall()
        cursor.close()
        conn.close()
        matchs = []
        if matchs_data:
            for match_data in matchs_data:
                confrontation_id = match_data[0]
                teamDomicile_id = match_data[1]
                teamExterieur_id = match_data[2]
                dateHeureDebut = match_data[3]
                dateHeureFin = match_data[4]
                statut = match_data[5]
                matchs.append(
                    Match(dateHeureDebut, dateHeureFin, statut, teamDomicile_id, teamExterieur_id, confrontation_id)
                )
            return matchs
        else:
            return None

    @staticmethod
    def getAllAVenir():
        conn = mysql.connect()
        cursor = conn.cursor()

        # Obtenir la date actuelle (aujourd'hui)
        cursor.execute("SELECT CURDATE()")

        # Récupérer la date actuelle
        current_date = cursor.fetchone()[0]

        # Sélectionner tous les matchs à venir (dateHeureDebut > aujourd'hui) avec le statut "Avenir"
        cursor.execute("SELECT * FROM Confrontation WHERE dateHeureDebut > %s AND statut = 'Avenir'", (current_date,))

        # Récupérer les matchs à venir
        upcoming_matchs_data = cursor.fetchall()

        conn.close()
        upcoming_matchs = []
        if upcoming_matchs_data:
            for upcoming_match_data in upcoming_matchs_data:
                confrontation_id = upcoming_match_data[0]
                teamDomicile_id = upcoming_match_data[1]
                teamExterieur_id = upcoming_match_data[2]
                dateHeureDebut = upcoming_match_data[3]
                dateHeureFin = upcoming_match_data[4]
                statut = upcoming_match_data[5]
                upcoming_matchs.append(
                    Match(dateHeureDebut, dateHeureFin, statut, teamDomicile_id, teamExterieur_id, confrontation_id)
                )
            return upcoming_matchs
        else:
            return None


    @staticmethod
    def get_match_by_teams(id_teamDomicile, id_teamExterieur):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from confrontation where equipeDomicileID=%s AND equipeExterieurID=%s",
            (id_teamDomicile, id_teamExterieur)
        )
        match_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if match_data:
            confrontation_id = match_data[0]
            teamDomicile_id = match_data[1]
            teamExterieur_id = match_data[2]
            dateHeureDebut = match_data[3]
            dateHeureFin = match_data[4]
            statut = match_data[5]
            return Match(dateHeureDebut, dateHeureFin, statut, teamDomicile_id, teamExterieur_id, confrontation_id)
        else:
            return None

    def update(self, id_teamDomicile, id_teamExterieur, dateHeureDebut, dateHeureFin, statut):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update confrontation set equipeDomicileID=%s, equipeExterieurID=%s, dateHeureDebut=%s, dateHeureFin=%s, statut=%s",
            (id_teamDomicile, id_teamExterieur, dateHeureDebut, dateHeureFin, statut)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def endMatch(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update confrontation set statut='Termine', dateHeureFin=NOW() where confrontationID=%s",
            (self.matchID,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def startMatch(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update confrontation set statut='EnCours' where confrontationID=%s",
            (self.matchID,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from confrontation where confrontationID=%s",
            (self.matchID,)
        )
        conn.commit()
        cursor.close()
        conn.close()


