from app import mysql


class User:
    def __init__(self, nom, prenom, adresseEmail, motDePasse, userID=None, dateInscription=None, actif=None):
        self.userID = userID
        self.nom = nom
        self.prenom = prenom
        self.adresseEmail = adresseEmail
        self.motDePasse = motDePasse
        self.dateInscription = dateInscription
        self.actif = actif

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createUser(%s, %s, %s, %s)",
            (self.nom, self.prenom, self.adresseEmail, self.motDePasse)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_email_actif(email):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Utilisateur WHERE adresseEmail = %s AND actif=1", (email,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            user_id = int(user_data[0])
            user_name = user_data[1]
            user_prenom = user_data[2]
            user_email = user_data[3]
            user_password = user_data[4]
            user_dateInscription = user_data[5]
            user_actif = user_data[6]
            return User(user_name, user_prenom, user_email, user_password, user_id, user_dateInscription, user_actif)
        else:
            return None

    @staticmethod
    def get_by_email_inactif(email):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Utilisateur WHERE adresseEmail = %s AND actif=0", (email,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            user_id = int(user_data[0])
            user_name = user_data[1]
            user_prenom = user_data[2]
            user_email = user_data[3]
            user_password = user_data[4]
            user_dateInscription = user_data[5]
            user_actif = user_data[6]
            return User(user_name, user_prenom, user_email, user_password, user_id, user_dateInscription, user_actif)
        else:
            return None

    @staticmethod
    def get_by_email(email):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Utilisateur WHERE adresseEmail = %s", (email,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            user_id = int(user_data[0])
            user_name = user_data[1]
            user_prenom = user_data[2]
            user_email = user_data[3]
            user_password = user_data[4]
            user_dateInscription = user_data[5]
            user_actif = user_data[6]
            return User(user_name, user_prenom, user_email, user_password, user_id, user_dateInscription, user_actif)
        else:
            return None

    @staticmethod
    def get_all_users_actif():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select * from utilisateur where actif=1")
        users_data = cursor.fetchall()
        cursor.close()
        conn.close()
        users = []
        if users_data:
            for user_data in users_data:
                user_id = int(user_data[0])
                user_name = user_data[1]
                user_prenom = user_data[2]
                user_email = user_data[3]
                user_password = user_data[4]
                user_dateInscription = user_data[5]
                user_actif = user_data[6]
                users.append(
                    User(user_name, user_prenom, user_email, user_password, user_id, user_dateInscription, user_actif))
            return users
        else:
            return None

    @staticmethod
    def get_all_users_inactif():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select * from utilisateur where actif=0")
        users_data = cursor.fetchall()
        cursor.close()
        conn.close()
        users = []
        if users_data:
            for user_data in users_data:
                user_id = int(user_data[0])
                user_name = user_data[1]
                user_prenom = user_data[2]
                user_email = user_data[3]
                user_password = user_data[4]
                user_dateInscription = user_data[5]
                user_actif = user_data[6]
                users.append(
                    User(user_name, user_prenom, user_email, user_password, user_id, user_dateInscription, user_actif))
            return users
        else:
            return None

    @staticmethod
    def get_all_users():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select * from utilisateur")
        users_data = cursor.fetchall()
        cursor.close()
        conn.close()
        users = []
        if users_data:
            for user_data in users_data:
                user_id = int(user_data[0])
                user_name = user_data[1]
                user_prenom = user_data[2]
                user_email = user_data[3]
                user_password = user_data[4]
                user_dateInscription = user_data[5]
                user_actif = user_data[6]
                users.append(
                    User(user_name, user_prenom, user_email, user_password, user_id, user_dateInscription, user_actif))
            return users
        else:
            return None

    @staticmethod
    def get_by_id(id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Utilisateur WHERE userID = %s", (id,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if user_data:
            user_id = int(user_data[0])
            user_name = user_data[1]
            user_prenom = user_data[2]
            user_email = user_data[3]
            user_password = user_data[4]
            user_dateInscription = user_data[5]
            user_actif = user_data[6]
            return User(user_name, user_prenom, user_email, user_password, user_id, user_dateInscription, user_actif)
        else:
            return None

    @staticmethod
    def update_user(nom, prenom, adresseEmail, motDePasse, emailBase):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Utilisateur SET nom=%s, prenom=%s, adresseEmail=%s, motDePasse=%s WHERE adresseEmail=%s",
            (nom, prenom, adresseEmail, motDePasse, emailBase)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete_user(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from utilisateur where adresseEmail=%s",
            (self.adresseEmail,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def desactivate_user(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update utilisateur set actif = 0 where adresseEmail = %s",
            (self.adresseEmail,)
        )
        conn.commit()
        cursor.close()
        conn.close()

