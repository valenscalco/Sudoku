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
            print("Para salir presione ENTER")
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
                if valido is False:
                    print("Ingrese un numero válido")
            while validor is False:
                x = int(input(
                    "Ingrese la fila para colocar el numero del 0 al 8 \n"))
                validor = self.validate_x(x)
                if validor is False:
                    print("Ingrese un numero válido")
            while validoc is False:
                y = int(input(
                    "Ingrese la columna para colocar el numero del 0 al 8 \n"))
                validoc = self.validate_y(y)
                if validoc is False:
                    print("Ingrese un numero válido")
            valp = self.sudoku.val_position(x, y)
            valr = self.sudoku.val_row(number, x)
            valc = self.sudoku.val_column(number, y)
            vala = self.sudoku.val_area(number, x, y)
            if vala is False:
                print("Numero repetido en el area")
            if valc is False:
                print("Numero repetido en la columna")
            if valr is False:
                print("Numero repetido en la fila")
            if valp is False:
                print("Posición original, ingrese ota posición")

            self.sudoku.val_variables(number, x, y)
        print("GANASTE")

    def validate(self, number):
        try:
            if number >= 1 and number <= 9:
                return True
            else:
                return False
        except Exception:
            return False

    def validate_x(self, x):
        try:
            if x >= 0 and x <= 8:
                return True
            else:
                return False
        except Exception:
            return False

    def validate_y(self, y):
        try:
            if y >= 0 and y <= 8:
                return True
            else:
                return False
        except Exception:
            return False


if __name__ == "__main__":
    Interfaz = Interfaz()
    Interfaz.run()
