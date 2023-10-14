from app import mysql


class Event:

    def __init__(self, description, dateHeure, type, matchID, eventID=None):
        self.description = description
        self.dateHeure = dateHeure
        self.type = type
        self.matchID = matchID
        self.eventID = eventID

    def save(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "CALL sp_createEvent(%s, %s, %s)",
            (self.description, self.type, self.matchID)
        )
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_by_id(eventID):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from evenement where eventID=%s",
            (eventID,)
        )
        event_data = cursor.fetchone()
        cursor.close()
        conn.close()
        if event_data:
            event_id = event_data[0]
            description = event_data[1]
            dateHeure = event_id[2]
            typeEvent = event_data[3]
            match_id = event_data[4]
            return Event(description, dateHeure, typeEvent, match_id, event_id)
        else:
            return None

    @staticmethod
    def get_all_by_match(matchID):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from evenement where confrontationID=%s",
            (matchID,)
        )
        events_data = cursor.fetchall()
        cursor.close()
        conn.close()
        events = []
        if events_data:
            for event_data in events_data:
                event_id = event_data[0]
                description = event_data[1]
                dateHeure = event_id[2]
                typeEvent = event_data[3]
                match_id = event_data[4]
                events.append(
                    Event(description, dateHeure, typeEvent, match_id, event_id)
                )
            return events
        else:
            return None

    @staticmethod
    def get_all():
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "select * from Evenement"
        )
        events_data = cursor.fetchall()
        cursor.close()
        conn.close()
        events = []
        if events_data:
            for event_data in events_data:
                event_id = event_data[0]
                description = event_data[1]
                dateHeure = event_id[2]
                typeEvent = event_data[3]
                match_id = event_data[4]
                events.append(
                    Event(description, dateHeure, typeEvent, match_id, event_id)
                )
            return events
        else:
            return None

    def update(self, description, typeEvent, match_id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "update evenement set descriptionEvenement=%s, typeEvenement=%s, dateHeureEvenement=NOW(), "
            "confrontationID=%s where eventID=%s",
            (description, typeEvent, match_id, self.eventID)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(
            "delete from Evenement where eventID=%s",
            (self.eventID,)
        )
        conn.commit()
        cursor.close()
        conn.close()