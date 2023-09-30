from app import mysql


class User:
    def __init__(self, nom, prenom, adresseEmail, motDePasse):
        self.nom = nom
        self.prenom = prenom
        self.adresseEmail = adresseEmail
        self.motDePasse = motDePasse

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Utilisateur (nom, prenom, adresseEmail, motDePasse) VALUES (%s, %s, %s, %s)",
            (self.nom, self.prenom, self.adresseEmail, self.motDePasse)
        )
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def get_by_id(user_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Utilisateur WHERE userID = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        if user_data:
            return User(*user_data)
        return None
