class Sudoku():
    def __init__(self, board):
        self.board = board

        self.no_delete = []
        for i in range(9):
            for j in range(len(self.board[i])):
                if (self.board[i][j] != 0):
                    self.no_delete.append((i, j))

    def val_position(self, x, y):
        if (x, y) in self.no_delete:
            return False
        else:
            return True

    def val_column(self, number, y):
        for i in range(9):
            if self.board[i][y] == number:
                return False

        return True

    def val_row(self, number, x):
        for j in range(9):
            if self.board[x][j] == number:
                return False

        return True

    def val_area(self, number, x, y):
        if x >= 0 and x <= 2:
            if y >= 0 and y <= 2:
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == number:
                            return False

                return True
            if y >= 3 and y <= 5:
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j+3] == number:
                            return False

                return True
            if y >= 6 and y <= 8:
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j+6] == number:
                            return False

                return True

        if x >= 3 and x <= 5:
            if y >= 0 and y <= 2:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+3][j] == number:
                            return False

                return True
            if y >= 3 and y <= 5:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+3][j+3] == number:
                            return False

                return True
            if y >= 6 and y <= 8:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+3][j+6] == number:
                            return False

                return True

        if x >= 6 and x <= 8:
            if y >= 0 and y <= 2:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+6][j] == number:
                            return False

                return True
            if y >= 3 and y <= 5:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+6][j+3] == number:
                            return False

                return True
            if y >= 6 and y <= 8:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+6][j+6] == number:
                            return False

                return True

    def val_variables(self, number, x, y):
        if (self.val_area(number, x, y) and self.val_column(number, y)
           and self.val_row(number, x) and self.val_position(x, y)):
            self.board[x][y] = number
            return True

    def val_win(self):
        cont = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    cont += 1
        if cont < 1:
            return True
        else:
            return False
