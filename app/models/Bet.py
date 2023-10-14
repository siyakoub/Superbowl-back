from app import mysql


class Bet:

    def __init__(self, userID, matchID, teamID, montantMiser, montantPotentiel, betID=None):
        self.userID = userID
        self.matchID = matchID
        self.teamID = teamID
        self.montantMiser = montantMiser
        self.montantPotentiel = montantPotentiel
        self.betID = betID

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createBet(%s, %s, %s, %s, %s)",
            (self.userID, self.matchID, self.teamID, self.montantMiser, self.montantPotentiel)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_id(bet_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from Pari where pariID=%s",
            (bet_id,)
        )
        bet_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if bet_data:
            bet_id = bet_data[0]
            userID = bet_data[1]
            matchID = bet_data[2]
            teamID = bet_data[3]
            montant_miser = bet_data[4]
            montant_potentiel = bet_data[5]
            return Bet(userID, matchID, teamID, montant_miser, montant_potentiel, bet_id)
        else:
            return None

    @staticmethod
    def get_all():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from Pari"
        )
        bets_data = cursor.fetchall()
        cursor.close()
        conn.close()
        bets = []
        if bets_data:
            for bet_data in bets_data:
                bet_id = bet_data[0]
                userID = bet_data[1]
                matchID = bet_data[2]
                teamID = bet_data[3]
                montant_miser = bet_data[4]
                montant_potentiel = bet_data[5]
                bets.append(
                    Bet(userID, matchID, teamID, montant_miser, montant_potentiel, bet_id)
                )
            return bets
        else:
            return None

    @staticmethod
    def get_all_by_user_id(userID):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from Pari where userID=%s",
            (userID,)
        )
        bets_data = cursor.fetchall()
        cursor.close()
        conn.close()
        bets = []
        if bets_data:
            for bet_data in bets_data:
                bet_id = bet_data[0]
                userID = bet_data[1]
                matchID = bet_data[2]
                teamID = bet_data[3]
                montant_miser = bet_data[4]
                montant_potentiel = bet_data[5]
                bets.append(
                    Bet(userID, matchID, teamID, montant_miser, montant_potentiel, bet_id)
                )
            return bets
        else:
            return None

    @staticmethod
    def get_all_by_match_id(match_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from Pari where confrontationID=%s",
            (match_id,)
        )
        bets_data = cursor.fetchall()
        cursor.close()
        conn.close()
        bets = []
        if bets_data:
            for bet_data in bets_data:
                bet_id = bet_data[0]
                userID = bet_data[1]
                matchID = bet_data[2]
                teamID = bet_data[3]
                montant_miser = bet_data[4]
                montant_potentiel = bet_data[5]
                bets.append(
                    Bet(userID, matchID, teamID, montant_miser, montant_potentiel, bet_id)
                )
            return bets
        else:
            return None

    @staticmethod
    def get_all_by_team_id(team_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from Pari where equipeID=%s",
            (team_id,)
        )
        bets_data = cursor.fetchall()
        cursor.close()
        conn.close()
        bets = []
        if bets_data:
            for bet_data in bets_data:
                bet_id = bet_data[0]
                userID = bet_data[1]
                matchID = bet_data[2]
                teamID = bet_data[3]
                montant_miser = bet_data[4]
                montant_potentiel = bet_data[5]
                bets.append(
                    Bet(userID, matchID, teamID, montant_miser, montant_potentiel, bet_id)
                )
            return bets
        else:
            return None

    def update(self, matchID, teamID, montant_miser, montant_potentiel):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update Pari set confrontationID=%s, equipeID=%s, montantMise=%s, montantGagnePerdu=%s where pariID=%s",
            (matchID, teamID, montant_miser, montant_potentiel, self.betID)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from Pari where pariID=%s",
            (self.betID,)
        )
        conn.commit()
        cursor.close()
        conn.close()






