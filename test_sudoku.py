import unittest
from sudoku import sudoku


class TestSudoku(unittest.TestCase):
    def test_game_not_over(self):
        sudoku = Sudoku(
            '53xx7xxxx'
            '6xx195xxx'
            'x98xxxx6x'
            '8xxx6xxx3'
            '4xx8x3xx1'
            '7xxx2xxx6'
            'x6xxxx28x'
            'xxx419xx5'
            'xxxx8xx79'
        )
        over = sudoku.is_over()
        self.assertFalse(over)

    def test_game_not_over1(self):
        sudoku = Sudoku(
            '53xx7xxxx'
            '6xx195xxx'
            'x98xxxx6x'
            '8xxx6xxx3'
            '4xx8x3xx1'
            '7xxx2xxx6'
            'x6xxxx28x'
            'xxx419xx5'
            'xxxx8xx79'
        )
        over = sudoku.is_over()
        self.assertFalse(over)

class Test_Sudoku(unittest.TestCase):
    def test_position_is_original(self):
        value = self.game.is_position_original(1, 1)
        self.assertTrue(value)

    def test_position_is_not_original(self):
        value = self.game.is_position_original(1, 3)
        self.assertFalse(value)

    def test_number_is_in_submatrix(self):
        value = self.game.is_in_area(5)
        self.assertTrue(value)

    def test_prove_number_is_not_in_submatrix(self):
        value = self.game.is_in_area(2)
        self.assertFalse(value)

    def test_prove_number_is_in_line(self):
        value = self.game.is_in_line(7)
        self.assertTrue(value)

    def test_prove_number_is_not_in_line(self):
        value = self.game.is_in_line(1)
        self.assertFalse(value)

    def test_prove_number_is_in_column(self):
        value = self.game.is_in_column(8)
        self.assertTrue(value)

    def test_prove_number_is_not_in_column(self):
        value = self.game.is_in_column(9)
        self.assertFalse(value)

    def test_number_load(self):
        x = 2
        y = 5
        load = self.game.test_number_load(x, y, 5)
        self.assertTrue(load)

    def test_state_win(self):
        state = self.game.is_over()
        self.assertTrue(state)

    def test_state_lose(self):
        state = self.game.is_over()
        self.assertFalse(state)


if __name__ == "__main__":
    unittest.main()
