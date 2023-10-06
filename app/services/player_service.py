from app.models.player import Player


class PlayerService:

    @staticmethod
    def create_player_service(name, firstName, numero, team_id):
        player = Player(name, firstName, numero, team_id)
        player.save()

    @staticmethod
    def get_all_player_service():
        return Player.get_all_player()

    @staticmethod
    def get_player_by_id_service(player_id):
        return Player.get_player_by_id(player_id)

    @staticmethod
    def get_player_by_name_complete_service(name, firstName):
        return Player.get_player_by_name_complete(name, firstName)

    @staticmethod
    def update_player_service(name, firstName, number, team_id):
        return Player.update_player(name, firstName, number, team_id)

    @staticmethod
    def delete_player_service(name, firstName):
        player = Player.get_player_by_name_complete(name, firstName)
        player.delete_player()