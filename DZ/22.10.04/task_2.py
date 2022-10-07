"""
Задача 2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
исходной последовательности.
"""


def input_numbers():
    while True:
        try:
            list_num = list(map(int, input("Введите числа через пробел: ").split()))
            return list_num
        except ValueError:
            print("Ошибка ввода")


def del_replay_num(list_numbers):
    new_list = []
    [new_list.append(i) for i in list_numbers if i not in new_list]
    return new_list


def main():
    start_list = input_numbers()
    print(f'Список введенных чисел: {start_list}')
    end_list = del_replay_num(start_list)
    print(f'Список с удалёнными повторами: {end_list}')


if __name__ == "__main__":
    main()