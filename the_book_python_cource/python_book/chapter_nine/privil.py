
class Privileges:

    def __init__(self):
        self.privileges = []

    def add_privilege(self, new_privilege):
        self.privileges.append(new_privilege)

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)