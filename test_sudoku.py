import unittest
from parameterized import parameterized
from sudoku import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self):

        self.sudoku = Sudoku([
            [5, 3, 0, 0, 0, 7, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ])

        self.sudoku1 = Sudoku([
            [5, 3, 4, 2, 6, 7, 1, 8, 9],
            [6, 8, 7, 1, 9, 5, 4, 3, 2],
            [1, 9, 8, 3, 4, 2, 7, 6, 5],
            [8, 1, 9, 7, 6, 5, 4, 2, 3],
            [4, 5, 6, 8, 7, 3, 2, 9, 1],
            [7, 3, 4, 1, 2, 8, 9, 3, 6],
            [4, 6, 3, 5, 7, 1, 2, 8, 9],
            [2, 8, 7, 4, 1, 9, 3, 6, 5],
            [1, 5, 6, 4, 8, 2, 3, 7, 9]
        ])

    @parameterized.expand([
        (0, 0),
        (0, 1),
        (0, 5),
        (1, 0),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 1),
        (2, 2),
        (2, 7),
        (3, 0),
        (3, 4),
        (3, 8),
        (4, 0),
        (4, 3),
        (4, 5),
        (4, 8),
        (5, 0),
        (5, 4),
        (5, 8),
        (6, 1),
        (6, 6),
        (6, 7),
        (7, 3),
        (7, 4),
        (7, 5),
        (7, 8),
        (8, 4),
        (8, 7),
        (8, 8)
    ])
    def test_position_is_original(self, x, y):
        # import pdb
        # pdb.set_trace()
        value = self.sudoku.val_position(x, y)
        self.assertFalse(value)

    @parameterized.expand([
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 6),
        (0, 7),
        (0, 8),
        (1, 1),
        (1, 2),
        (1, 6),
        (1, 7),
        (1, 8),
        (2, 0),
        (2, 3),
        (2, 4),
        (2, 5),
        (2, 6),
        (2, 8),
        (3, 1),
        (3, 2),
        (3, 3),
        (3, 5),
        (3, 6),
        (3, 7),
        (4, 1),
        (4, 2),
        (4, 4),
        (4, 6),
        (4, 7),
        (5, 1),
        (5, 2),
        (5, 3),
        (5, 5),
        (5, 6),
        (5, 7),
        (6, 0),
        (6, 2),
        (6, 3),
        (6, 4),
        (6, 5),
        (6, 8),
        (7, 0),
        (7, 1),
        (7, 2),
        (7, 6),
        (7, 7),
        (8, 0),
        (8, 1),
        (8, 2),
        (8, 3),
        (8, 5),
        (8, 6)
    ])
    def test_position_is_not_original(self, x, y):
        value = self.sudoku.val_position(x, y)
        self.assertTrue(value)

    def test_number_is_not_in_submatrix(self):
        value = self.sudoku.val_area(7, 1, 1)
        self.assertTrue(value)

    def test_prove_number_is_in_submatrix(self):
        value = self.sudoku.val_area(3, 3, 5)
        self.assertFalse(value)

    def test_prove_number_is_not_in_row(self):
        value = self.sudoku.val_row(7, 2)
        self.assertTrue(value)

    def test_prove_number_is_in_row(self):
        value = self.sudoku.val_row(8, 8)
        self.assertFalse(value)

    def test_prove_number_is_not_in_column(self):
        value = self.sudoku.val_column(8, 8)
        self.assertTrue(value)

    def test_prove_number_is_in_column(self):
        value = self.sudoku.val_column(9, 8)
        self.assertFalse(value)

    def test_number_load(self):
        x = 6
        y = 2
        load = self.sudoku.val_variables(5, x, y)
        self.assertTrue(load)

    def test_state_win(self):
        state = self.sudoku1.val_win()
        self.assertTrue(state)

    def test_state_lose(self):
        state = self.sudoku.val_win()
        self.assertFalse(state)


if __name__ == "__main__":
    unittest.main()
