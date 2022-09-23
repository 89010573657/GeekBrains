"""задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
для всех значений предикат."""


def check_statements(x, y, z):
    result = not(z or y or z) == (not x and not y and not z)
    if result:
        string = "ИСТИННО"
    else:
        string = "ЛОЖНО"
    print(f"""Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z {string} при входных данных равных:
X = {bool(x)}
Y = {bool(y)}
Z = {bool(z)}
-------------------------------------------------------------------------""")


check_statements(0, 0, 0)
check_statements(1, 0, 0)
check_statements(0, 1, 0)
check_statements(0, 0, 1)
check_statements(1, 1, 0)
check_statements(1, 0, 1)
check_statements(0, 1, 1)
check_statements(1, 1, 1)
