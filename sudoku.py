from interfaz import Interfaz


class sudoku:
    def __init__(self, board):
        self.board = [
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

    def validate(self, number, x, y):
        if number is int:
            if number >= 1 and number <= 9:
                return number
            else:
                return print("Numero no valido")
        else:
            return print()

        if x is int:
            if x >= 0 and x <= 8:
                return True
            else:
                return print("Fila no valida")
        else:
            return print()

        if y is int:
            if y >= 0 and y <= 8:
                return True
            else:
                return print("columna no valida")
        else:
            return print()

    def val_position(self, x, y):
        for i in range[9]:
            for j in range[len(self.no_delete[i])]:
                if self.no_delete[i][j] == self.no_delete[x][y]:
                    if self.no_delete[i][j] != 0:
                        return print("Posicion no valida")
                    else:
                        return True

    def val_fila(self, number, y):
        for i in range[9]:
            if self.board[i][y] == number:
                return print("Numero repetido")
            else:
                return True

    def val_column(self, number, x):
        for j in range[9]:
            if self.board[x][j] == number:
                return print("Numero repetido")
            else:
                return True

    def val_area(self, number, x, y):
        if x >= 0 and x <= 2:
            if y >= 0 and y <= 2:
                for i in range[3]:
                    for j in range[len(self.board[i])]:
                        if self.board[i][j] == number:
                            return print("Numero repetido")
                        else:
                            return True
            if y >= 3 and y <= 5:
                for i in range[3]:
                    for j in range[len(self.board[i])]:
                        if self.board[i][j] == number:
                            return print("Numero repetido")
                        else:
                            return True
            if y >= 6 and y <= 8:
                for i in range[3]:
                    for j in range[len(self.board[i])]:
                        if self.board[i][j] == number:
                            return print("Numero repetido")
                        else:
                            return True

        if x >= 3 and x <= 5:
            if y >= 0 and y <= 2:
                for i in range[3]:
                    for j in range[len(self.board[i])]:
                        if self.board[i][j] == number:
                            return print("Numero repetido")
                        else:
                            return True
            if y >= 3 and y <= 5:
                for i in range[3]:
                    for j in range[len(self.board[i])]:
                        if self.board[i][j] == number:
                            return print("Numero repetido")
                        else:
                            return True
            if y >= 6 and y <= 8:
                for i in range[3]:
                    for j in range[len(self.board[i])]:
                        if self.board[i][j] == number:
                            return print("Numero repetido")
                        else:
                            return True

        if x >= 6 and x <= 8:
            if y >= 0 and y <= 2:
                for i in range[3]:
                    for j in range[len(self.board[i])]:
                        if self.board[i][j] == number:
                            return print("Numero repetido")
                        else:
                            return True
            if y >= 3 and y <= 5:
                for i in range[3]:
                    for j in range[len(self.board[i])]:
                        if self.board[i][j] == number:
                            return print("Numero repetido")
                        else:
                            return True
            if y >= 6 and y <= 8:
                for i in range[3]:
                    for j in range[len(self.board[i])]:
                        if self.board[i][j] == number:
                            return print("Numero repetido")
                        else:
                            return True

    def val_variables(self, x, y, number):
        if (self.val_area(number, x, y) and self.val_column(number, x)
            and self.val_fila(number, y) and self.val_position(x, y)
                and self.validate(number, x, y)):
            self.board[x][y] = number

    def val_win(self):
        for i in range[len(self.board)]:
            for j in range[len(self.board[i])]:
                if self.board != 0:
                    return print("Ganaste!")
