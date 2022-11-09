def commands():
    command = input("Нажмите Enter для продолжения vs Любое значение для закрытия программы: ")
    if command != "":
        print("Всего хорошего")
        return exit()


def input_data():
    try:
        num_1 = float(input("Введите первое число: "))
        num_2 = float(input("Введите второе число: "))
        operation = input("""Введите операцию над этими двумя числами! Поддерживаемые операции: 
        + - Плюс,
        - - Минус,
        / - Деление,
        * - Умножение,
        mod - взятие остатка от деления,
        pow — возведение в степень,
        div — целочисленное деление
        Ввод операции: """)
        if operation not in ['+', '-', '/', '*', 'mod', 'pow', 'div']:
            print("Данная операция не поддерживается!!!")
            commands()
        return num_1, num_2, operation

    except ValueError:
        print("Ошибка ввода - вы ввели не вещественное число!")
        commands()


def calculator(num_1, num_2, operation):

    match operation:
        case '+':
            return f"{num_1} + {num_2} = {num_1 + num_2}"
        case '-':
            return f"{num_1} - {num_2} = {num_1 - num_2}"
        case '/':
            return f"{num_1} / {num_2} = {num_1 / num_2}"
        case '*':
            return f"{num_1} * {num_2} = {num_1 * num_2}"
        case 'mod':
            return f"{num_1} mod {num_2} = {num_1 % num_2}"
        case 'pow':
            return f"{num_1} pow {num_2} = {num_1 ** num_2}"
        case 'div':
            return f"{num_1} div {num_2} = {num_1 // num_2}"
        case _:
            return "Данная операция не поддерживается!!!"


def main():
    while True:
        commands()
        data = input_data()
        print(type(data))
        print(calculator(data[0], data[1], data[2]))
        commands()


if __name__ == "__main__":
    main()