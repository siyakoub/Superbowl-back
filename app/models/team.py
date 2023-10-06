from app import mysql


class Team:

    def __init__(self, name, country, teamID=None):
        self.name = name
        self.country = country
        self.teamID = teamID

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createEquipe(%s, %s)",
            (self.name, self.country)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_equipe_by_id(id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from equipe where equipeID = %s",
            (id,)
        )
        team_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if team_data:
            team_id = team_data[0]
            team_name = team_data[1]
            team_country = team_data[2]
            return Team(team_name, team_country, team_id)
        else:
            return None

    @staticmethod
    def get_team_by_name(name):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from equipe where nomEquipe = %s",
            (name,)
        )
        team_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if team_data:
            team_id = team_data[0]
            team_name = team_data[1]
            team_country = team_data[2]
            return Team(team_name, team_country, team_id)
        else:
            return None

    @staticmethod
    def get_all_team():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from equipe"
        )
        teams_data = cursor.fetchall()
        cursor.close()
        conn.close()
        teams = []
        if teams_data:
            for team_data in teams_data:
                team_id = team_data[0]
                team_name = team_data[1]
                team_country = team_data[2]
                teams.append(
                    Team(team_name, team_country, team_id)
                )
            return teams
        else:
            return None

    def update_team(self, name, country):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE equipe set nomEquipe = %s, paysOrigine = %s where equipeID = %s",
            (name, country, self.teamID)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete_team(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from equipe where equipeID = %s",
            (self.teamID,)
        )
        conn.commit()
        cursor.close()
        conn.close()