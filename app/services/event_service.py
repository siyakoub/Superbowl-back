import datetime

from app.models.event import Event


class EventService:


    @staticmethod
    def create_event_service(description, type, matchID):
        event = Event(description, datetime.datetime.now(), type, matchID)
        event.save()

    @staticmethod
    def update_event_service(eventID, description, type, matchID):
        event = Event.get_by_id(eventID)
        if event:
            event.update(description, type, matchID)
        else:
            pass

    @staticmethod
    def delete_event_service(eventID):
        event = Event.get_by_id(eventID)
        if event:
            event.delete()
        else:
            pass

    @staticmethod
    def get_all_event_service():
        return Event.get_all()

    @staticmethod
    def get_all_event_by_match_id(match_id):
        return Event.get_all_by_match(match_id)

    @staticmethod
    def get_event_by_id(event_id):
        return Event.get_by_id(event_id)