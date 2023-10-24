from app import mysql


class Session:
    def __init__(self, email, token, dateHeureDebut, dateHeureFin, sessionID=None):
        self.email = email
        self.token = token
        self.dateHeureDebut = dateHeureDebut
        self.dateHeureFin = dateHeureFin
        self.sessionID = sessionID

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createSession(%s, %s, %s, %s)",
            (self.email, self.token, self.dateHeureDebut, self.dateHeureFin)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_id(session_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from session where sessionID=%s",
            (session_id,)
        )
        session_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if session_data:
            sessionID = session_data[0]
            email = session_data[1]
            token = session_data[2]
            dateHeureDebut = session_data[3]
            dateHeureFin = session_data[4]
            return Session(email, token, dateHeureDebut, dateHeureFin, sessionID)
        else:
            return None

    @staticmethod
    def get_all_by_email(email):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from superBowlBdd.session where email=%s",
            (email,)
        )
        sessions_data = cursor.fetchall()
        cursor.close()
        conn.close()
        sessions = []
        if sessions_data:
            for session_data in sessions_data:
                sessionID = session_data[0]
                email_data = session_data[1]
                token = session_data[2]
                dateHeureDebut = session_data[3]
                dateHeureFin = session_data[4]
                sessions.append(
                    Session(email_data, token, dateHeureDebut, dateHeureFin, sessionID)
                )
            return sessions
        else:
            return None

    @staticmethod
    def get_all():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from session"
        )
        sessions_data = cursor.fetchall()
        cursor.close()
        conn.close()
        sessions = []
        if sessions_data:
            for session_data in sessions_data:
                sessionID = session_data[0]
                email = session_data[1]
                token = session_data[2]
                dateHeureDebut = session_data[3]
                dateHeureFin = session_data[4]
                sessions.append(
                    Session(email, token, dateHeureDebut, dateHeureFin, sessionID)
                )
            return sessions
        else:
            return None

    @staticmethod
    def get_by_token(token):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from superBowlBdd.session where token=%s",
            (token,)
        )
        session_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if session_data:
            sessionID = session_data[0]
            email = session_data[1]
            token = session_data[2]
            dateHeureDebut = session_data[3]
            dateHeureFin = session_data[4]
            return Session(email, token, dateHeureDebut, dateHeureFin, sessionID)
        else:
            return None

    def update(self, email, token, dateHeureFin):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update session set email=%s, token=%s, dateHeureFin=%s where sessionID=%s",
            (email, token, dateHeureFin, self.sessionID)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from session where sessionID=%s",
            (self.sessionID,)
        )
        conn.commit()
        cursor.close()
        conn.close()


