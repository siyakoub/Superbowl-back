from app import mysql

class Player:

    def __init__(self, name, firstName, number, team_ID, playerID=None):
        self.name = name
        self.firstName = firstName
        self.number = number
        self.team_ID = team_ID
        self.playerID = playerID

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createJoueur(%s, %s, %s, %s)",
            (self.name, self.firstName, self.number, self.team_ID)
        )
        conn.commit()
        cursor.close()
        conn.close()


    @staticmethod
    def get_player_by_id(player_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from joueur where joueurID=%s",
            (player_id,)
        )
        player_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if player_data:
            player_id = player_data[0]
            player_name = player_data[1]
            player_firstName = player_data[2]
            player_number = player_data[3]
            team_id = player_data[4]
            return Player(player_name, player_firstName, player_number, team_id, player_id)
        else:
            return None


    @staticmethod
    def get_player_by_name_complete(name, firstName):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from joueur where nomJoueur = %s AND prenomJoueur = %s",
            (name, firstName)
        )
        player_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if player_data:
            player_id = player_data[0]
            player_name = player_data[1]
            player_firstName = player_data[2]
            player_number = player_data[3]
            team_id = player_data[4]
            return Player(player_name, player_firstName, player_number, team_id, player_id)
        else:
            return None

    @staticmethod
    def get_all_player():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from joueur"
        )
        players_data = cursor.fetchall()
        cursor.close()
        conn.close()
        players = []
        if players_data:
            for player_data in players_data:
                player_id = player_data[0]
                player_name = player_data[1]
                player_firstName = player_data[2]
                player_number = player_data[3]
                team_id = player_data[4]
                players.append(
                    Player(player_name, player_firstName, player_number, team_id, player_id)
                )
            return players
        else:
            return None

    def update_player(self, name, firstName, number, team_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE joueur set nomJoueur=%s, prenomJoueur=%s, numeroJoueur=%s, equipeID=%s where joueurID=%s",
            (name, firstName, number, team_id, self.playerID)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete_player(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from joueur where joueurID=%s",
            (self.playerID,)
        )
        conn.commit()
        cursor.close()
        conn.close()
