from app import mysql


class Admin:

    def __init__(self, login, password, nom, prenom, adminID=None, actif=None):
        self.login = login
        self.password = password
        self.nom = nom
        self.prenom = prenom
        self.adminID = adminID
        self.actif = actif

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createAdmin(%s, %s, %s, %s)",
            (self.login, self.password, self.nom, self.prenom)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_admin_actif_by_login(login):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM administrateur WHERE login = %s AND actif=1", (login,))
        admin_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if admin_data:
            admin_id = int(admin_data[0])
            admin_login = admin_data[1]
            admin_password = admin_data[2]
            admin_name = admin_data[3]
            admin_firstname = admin_data[4]
            admin_actif = admin_data[5]
            return Admin(admin_login, admin_password, admin_name, admin_firstname, admin_id, admin_actif)
        else:
            return None

    @staticmethod
    def get_all_admin_actif():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select * from administrateur where actif=1")
        admins_data = cursor.fetchall()
        cursor.close()
        conn.close()
        admins = []
        if admins_data:
            for admin_data in admins_data:
                admin_id = int(admin_data[0])
                admin_login = admin_data[1]
                admin_password = admin_data[2]
                admin_name = admin_data[3]
                admin_firstname = admin_data[4]
                admin_actif = admin_data[5]
                admins.append(
                    Admin(admin_login, admin_password, admin_name, admin_firstname, admin_id, admin_actif))
            return admins
        else:
            return None

    @staticmethod
    def get_all_admin_inactif():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select * from administrateur where actif=0")
        admins_data = cursor.fetchall()
        cursor.close()
        conn.close()
        admins = []
        if admins_data:
            for admin_data in admins_data:
                admin_id = int(admin_data[0])
                admin_login = admin_data[1]
                admin_password = admin_data[2]
                admin_name = admin_data[3]
                admin_firstname = admin_data[4]
                admin_actif = admin_data[5]
                admins.append(
                    Admin(admin_login, admin_password, admin_name, admin_firstname, admin_id, admin_actif))
            return admins
        else:
            return None

    @staticmethod
    def get_all_admin():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("select * from administrateur")
        admins_data = cursor.fetchall()
        cursor.close()
        conn.close()
        admins = []
        if admins_data:
            for admin_data in admins_data:
                admin_id = int(admin_data[0])
                admin_login = admin_data[1]
                admin_password = admin_data[2]
                admin_name = admin_data[3]
                admin_firstname = admin_data[4]
                admin_actif = admin_data[5]
                admins.append(
                    Admin(admin_login, admin_password, admin_name, admin_firstname, admin_id, admin_actif))
            return admins
        else:
            return None

    @staticmethod
    def get_by_id(id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM administrateur WHERE administrateurID = %s", (id,))
        admin_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if admin_data:
            admin_id = int(admin_data[0])
            admin_login = admin_data[1]
            admin_password = admin_data[2]
            admin_name = admin_data[3]
            admin_firstname = admin_data[4]
            admin_actif = admin_data[5]
            return Admin(admin_login, admin_password, admin_name, admin_firstname, admin_id, admin_actif)
        else:
            return None

    @staticmethod
    def get_admin_inactif_by_login(login):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM administrateur where login=%s AND actif=0",
            (login,)
        )
        admin_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if admin_data:
            admin_id = int(admin_data[0])
            admin_login = admin_data[1]
            admin_password = admin_data[2]
            admin_name = admin_data[3]
            admin_firstname = admin_data[4]
            admin_actif = admin_data[5]
            return Admin(admin_login, admin_password, admin_name, admin_firstname, admin_id, admin_actif)
        else:
            return None

    @staticmethod
    def get_admin_by_login(login):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM administrateur where login=%s",
            (login,)
        )
        admin_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if admin_data:
            admin_id = int(admin_data[0])
            admin_login = admin_data[1]
            admin_password = admin_data[2]
            admin_name = admin_data[3]
            admin_firstname = admin_data[4]
            admin_actif = admin_data[5]
            return Admin(admin_login, admin_password, admin_name, admin_firstname, admin_id, admin_actif)
        else:
            return None

    def update_admin(self, login, password, name, firstname):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE administrateur SET login=%s, pass=%s, nom=%s, prenom=%s where login=%s",
            (login, password, name, firstname, self.login)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete_admin(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM administrateur where login=%s",
            (self.login,)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def desactivate_admin(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE administrateur SET actif = 0 where login=%s",
            (self.login,)
        )
        conn.commit()
        cursor.close()
        conn.close()






