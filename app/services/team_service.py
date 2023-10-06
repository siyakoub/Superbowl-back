from app.models.team import Team

class TeamService:

    @staticmethod
    def create_team_service(name, country):
        team = Team(name, country)
        team.save()

    @staticmethod
    def update_team_service(name, country):
        return Team.update_team(name, country)

    @staticmethod
    def get_team_by_id_service(id):
        return Team.get_equipe_by_id(id)

    @staticmethod
    def get_team_by_name_service(name):
        return Team.get_team_by_name(name)

    @staticmethod
    def get_all_teams():
        return Team.get_all_team()

    @staticmethod
    def delete_admin_by_id_service(name):
        team = Team.get_team_by_name(name)
        return team.delete_team()
