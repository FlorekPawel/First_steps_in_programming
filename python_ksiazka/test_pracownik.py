import unittest
from pracownik import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.employee = Employee('paweł', 'florek', 4000)
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.pensja, 9000)

    def test_give_custom_raise(self):
        self.employee.give_raise(2000)
        self.assertEqual(self.employee.pensja, 6000)

unittest.main()