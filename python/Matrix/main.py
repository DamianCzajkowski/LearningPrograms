from matrix import Matrix
from exceptions import MatrixOperationException, MatrixIndexException


def menu():
    while True:
        case = input("""1) Wczytaj macierz A
                        2) Wczytaj macierz B
                        3) Wyświetl A
                        4) Wyświetl B
                        5) Wykonaj A+B
                        6) Wykonaj A*B
                        7) Wyjście\n""")
        if case == "1":
            n = int(input("podaj n: "))
            m = int(input("podaj m: "))
            m1 = Matrix(n, m)
            for row in range(n):
                for col in range(m):
                    v = float(input(f"podaj wartość na pozycji [{row}, {col}]: "))
                    try:
                        m1.set_value(r=row, c=col, value=v)
                    except MatrixIndexException:
                        print("Błąd!")
                        break
                else:
                    continue
                break
        elif case == "2":
            n = int(input("podaj n: "))
            m = int(input("podaj m: "))
            m2 = Matrix(n, m)
            for row in range(n):
                for col in range(m):
                    v = float(input(f"podaj wartość na pozycji [{row}, {col}]: "))
                    try:
                        m2.set_value(r=row, c=col, value=v)
                    except MatrixIndexException:
                        print("Błąd!")
                        break
                else:
                    continue
                break
        elif case == "3":
            print(m1)
        elif case == "4":
            print(m2)
        elif case == "5":
            try:
                result = m1 + m2
            except MatrixOperationException:
                print("Błąd!")
                break
            for value in result:
                print(value, end=" ")
            print("\n")
            for row in result.rows():
                print(row)
        elif case == "6":
            try:
                result = m1 * m2
            except MatrixOperationException:
                print("Błąd!")
                break
            for value in result:
                print(value, end=" ")
            print("\n")
            for row in result.rows():
                print(row)
        elif case == "7":
            return


if __name__ == "__main__":
    menu()
