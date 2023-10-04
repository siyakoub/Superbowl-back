from app.models.admin import Admin

class AdminService:
    @staticmethod
    def create_admin(login, password, nom, prenom):
        admin = Admin(login, password, nom, prenom)
        admin.save()

    @staticmethod
    def get_admin_actif_by_login(login):
        return Admin.get_admin_actif_by_login(login)

    @staticmethod
    def get_all_admin_actif():
        return Admin.get_all_admin_actif()

    @staticmethod
    def get_all_admin_inactif():
        return Admin.get_all_admin_inactif()

    @staticmethod
    def get_admin_by_login(login):
        return Admin.get_admin_by_login(login)

    @staticmethod
    def get_admin_inactif_by_login(login):
        return Admin.get_admin_inactif_by_login(login)

    @staticmethod
    def update_admin(login, password, name, firstname):
        admin = Admin.get_admin_actif_by_login(login)
        if admin:
            admin.update_admin(login, password, name, firstname)
        else:
            pass

    @staticmethod
    def delete_admin(admin):
        if admin:
            admin.delete_admin()
        else:
            pass

    @staticmethod
    def desactivate_admin(admin):
        if admin:
            admin.desactivate_admin()
        else:
            pass
