from app import mysql


class Odds:

    def __init__(self, coteVictoire: float, teamID: int, coteID=None):
        self.coteVictoire = coteVictoire
        self.teamID = teamID
        self.coteID = coteID

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createCote(%s, %s)",
            (self.coteVictoire, self.teamID)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, coteVictoire):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE cote set coteVictoire=%s where coteID=%s",
            (coteVictoire, self.coteID)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_id(coteId):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from cote where coteID=%s",
            (coteId,)
        )
        cote_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if cote_data:
            cote_id = cote_data[0]
            cote_victoire = cote_data[1]
            team_id = cote_data[2]
            return Odds(team_id, cote_victoire, cote_id)
        else:
            return None

    @staticmethod
    def get_by_team(team_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from cote where equipeID=%s",
            (team_id,)
        )
        cote_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if cote_data:
            cote_id = cote_data[0]
            cote_victoire = cote_data[2]
            good_team_id = cote_data[1]
            return Odds(cote_victoire, good_team_id, cote_id)
        else:
            return None

    @staticmethod
    def get_all():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from cote"
        )
        cotes_data = cursor.fetchall()
        cursor.close()
        conn.close()
        cotes = []
        if cotes_data:
            for cote_data in cotes_data:
                cote_id = cote_data[0]
                cote_victoire = cote_data[1]
                team_id = cote_data[2]
                cotes.append(
                    Odds(team_id, cote_victoire, cote_id)
                )
            return cotes
        else:
            return None

    def delete_odds(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from cote where coteID=%s",
            (self.coteID,)
        )
        conn.commit()
        cursor.close()
        conn.close()
