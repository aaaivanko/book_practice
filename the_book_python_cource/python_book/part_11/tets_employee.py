import unittest
from workers import Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.new_emp = Employee('ivan', 'bob')

    def test_give_default_raise(self):
        default_salary = self.new_emp.give_raise()
        self.assertEqual(default_salary, 5000)

    def test_give_custom_raise(self):
        custom_raise = self.new_emp.give_raise(45)
        self.assertEqual(custom_raise, 45)
