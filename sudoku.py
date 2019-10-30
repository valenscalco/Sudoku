class Sudoku():
    def __init__(self, board):
        self.board = board

        self.no_delete = [
            [5, 3, 0, 0, 0, 7, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

    def val_position(self, x, y):
        if self.no_delete[x][y] != 0:
            print("Posicion original, coloque otra posicion")
            return False
        else:
            return True

    def val_column(self, number, y):
        for i in range(9):
            if self.board[i][y] == number:
                print("Se repite el numero en la columna")
                return False

        return True

    def val_row(self, number, x):
        for j in range(9):
            if self.board[x][j] == number:
                print("Se repite el numero en la fila")
                return False

        return True

    def val_area(self, number, x, y):
        if x >= 0 and x <= 2:
            if y >= 0 and y <= 2:
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j] == number:
                            print("Se repite el numero en el area")
                            return False

                return True
            if y >= 3 and y <= 5:
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j+3] == number:
                            print("Se repite el numero en el area")
                            return False

                return True
            if y >= 6 and y <= 8:
                for i in range(3):
                    for j in range(3):
                        if self.board[i][j+6] == number:
                            print("Se repite el numero en el area")
                            return False

                return True

        if x >= 3 and x <= 5:
            if y >= 0 and y <= 2:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+3][j] == number:
                            print("Se repite el numero en el area")
                            return False

                return True
            if y >= 3 and y <= 5:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+3][j+3] == number:
                            print("Se repite el numero en el area")
                            return False

                return True
            if y >= 6 and y <= 8:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+3][j+6] == number:
                            print("Se repite el numero en el area")
                            return False

                return True

        if x >= 6 and x <= 8:
            if y >= 0 and y <= 2:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+6][j] == number:
                            print("Se repite el numero en el area")
                            return False

                return True
            if y >= 3 and y <= 5:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+6][j+3] == number:
                            print("Se repite el numero en el area")
                            return False

                return True
            if y >= 6 and y <= 8:
                for i in range(3):
                    for j in range(3):
                        if self.board[i+6][j+6] == number:
                            print("Se repite el numero en el area")
                            return False

                return True

    def val_variables(self, number, x, y):
        if (self.val_area(number, x, y) and self.val_column(number, x)
           and self.val_row(number, y) and self.val_position(x, y)):
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
