import unittest
from interfaz import Interfaz


class Test_Interfaz(unittest.TestCase):
    def setUp(self):
        self.interfaz = Interfaz()

    def test_num_valid(self):
        value = self.interfaz.validate(4)
        self.assertTrue(value)

    def test_num_NO_valid(self):
        value = self.interfaz.validate('a')
        self.assertFalse(value)

    def test_row_valid(self):
        value = self.interfaz.validate_x(1)
        self.assertTrue(value)

    def test_row_NO_valid(self):
        value = self.interfaz.validate_x(11)
        self.assertFalse(value)

    def test_column_valid(self):
        value = self.interfaz.validate_y(2)
        self.assertTrue(value)

    def test_column_NO_valid(self):
        value = self.interfaz.validate_y(9)
        self.assertFalse(value)


if __name__ == "__main__":
    unittest.main()
