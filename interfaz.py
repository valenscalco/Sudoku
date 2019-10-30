from sudoku import Sudoku
from api import api


class Interfaz(Sudoku):

    def __init__(self):
        lista = api(9)
        self.sudoku = Sudoku(lista)

    def display(self):
        u = 0
        for i in range(1):
            print('\t')
        for j in range(9):
            u += 1
            if u == 4 or u == 7:
                print('--------+---------+--------')
            print(self.sudoku.board[j], )
        print("\n")

    def run(self):
        x = 0
        y = 0
        number = 0
        while not self.sudoku.val_win():
            self.display()
            valido = False
            validoc = False
            validor = False
            while valido is False:
                number = int(input("Ingrese un numero entre el 1 al 9\n"))
                valido = Interfaz.validate(number)
            while validoc is False:
                x = int(input(
                    "Ingrese la fila para colocar el numero del 0 al 8 \n"))
                validoc = self.validate_x(x)
            while validor is False:
                y = int(input(
                    "Ingrese la columna para colocar el numero del 0 al 8 \n"))
                validor = self.validate_y(y)

            self.sudoku.val_variables(number, x, y)

    def validate(self, number):
        try:
            if number >= 1 and number <= 9:
                return True
            else:
                print("Ingrese un numero entre 0 y 9")
                return False
        except Exception:
            return False

    def validate_x(self, x):
        if x:
            if x >= 0 and x <= 8:
                return True
            else:
                print("Ingrese un numero entre 0 y 8")
                return False
        else:
            print("Ingrese un numero porfavor")
            return False

    def validate_y(self, y):
        if y:
            if y >= 0 and y <= 8:
                return True
            else:
                print("Ingrese un numero entre 0 y 8")
                return False
        else:
            print("Ingrese un numero porfavor")
            return False


if __name__ == "__main__":
    Interfaz = Interfaz()
    Interfaz.run()
