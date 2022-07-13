
class Employee:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.year_salary = 0

    def give_raise(self, salary_raise=None):
        if salary_raise:
            self.year_salary += salary_raise
        else:
            self.year_salary = 5_000
        return self.year_salary
