from app import mysql


class User:
    def __init__(self, nom, prenom, adresseEmail, motDePasse, userID=None, dateInscription=None):
        self.userID = userID
        self.nom = nom
        self.prenom = prenom
        self.adresseEmail = adresseEmail
        self.motDePasse = motDePasse
        self.dateInscription = dateInscription

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createUser(%s, %s, %s, %s)",
            (self.nom, self.prenom, self.adresseEmail, self.motDePasse)
        )
        conn.commit()
        cursor.close()

    @staticmethod
    def get_by_email(email):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Utilisateur WHERE adresseEmail = %s", (email,))
        user_data = cursor.fetchone()
        cursor.close()
        if user_data:
            user_id = int(user_data[0])
            user_name = user_data[1]
            user_prenom = user_data[2]
            user_email = user_data[3]
            user_password = user_data[4]
            user_dateInscription = user_data[5]
            return User(user_name, user_prenom, user_email, user_password, user_id, user_dateInscription)
        else:
            return None

