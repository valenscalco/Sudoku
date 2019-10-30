import unittest
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

    def test_position_is_original(self):
        # import pdb
        # pdb.set_trace()
        value = self.sudoku.val_position(0, 0)
        self.assertFalse(value)

    def test_position_is_not_original(self):
        value = self.sudoku.val_position(1, 2)
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
