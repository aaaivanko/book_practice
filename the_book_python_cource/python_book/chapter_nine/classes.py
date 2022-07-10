from battery import Battery
from privil import Privileges


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Admin(User):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.privileges = Privileges()


new_admin = Admin('ivan', 15)

new_admin.privileges.add_privilege('can delete user')
new_admin.privileges.add_privilege('can update user info')

new_admin.privileges.show_privileges()


