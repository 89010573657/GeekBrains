def commands():
    command = input("Нажмите Enter для продолжения vs Любое значение для закрытия программы: ")
    if command != "":
        print("Всего хорошего")
        return exit()


def calculator():

    commands()

    try:
        num_1 = float(input("Введите первое число: "))
        num_2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка ввода - вы ввели не вещественное число!")
        commands()
    operation = input("""Введите операцию над этими двумя числами! Поддерживаемые операции: 
    + - Плюс,
    - - Минус,
    / - Деление,
    * - Умножение,
    mod - взятие остатка от деления,
    pow — возведение в степень,
    div — целочисленное деление
    Ввод операции: """)

    if operation not in ["+", "-", "/", "*", "mod", "div", "pow"]:
        print("Данная операция не поддерживается!!!")
        commands()

    if operation == '+':
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    elif operation == '-':
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    elif operation == '/':
        print(f"{num_1} / {num_2} = {num_1 / num_2}")
    elif operation == '*':
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
    elif operation == 'mod':
        print(f"{num_1} mod {num_2} = {num_1 % num_2}")
    elif operation == 'pow':
        print(f"{num_1} pow {num_2} = {num_1 ** num_2}")
    elif operation == 'div':
        print(f"{num_1} div {num_2} = {num_1 // num_2}")
    commands()


print(calculator())
