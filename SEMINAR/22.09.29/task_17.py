"""# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число."""
from random import randint


def get_numbers():
    try:
        numbers = int(input("Введите целое число: "))
        return numbers
    except ValueError:
        print("Ошибка ввода")


def get_fill_list(n):
    fill_list = []
    for i in range(0, n):
        fill_list.append(randint(-n, n))
    return fill_list


def read_file():
    file = open('file.txt', 'r')
    list = []
    for line in file:
        list.append(int(line))
    return list


def main():
    fill_list = get_fill_list(get_numbers())
    print(f'Сформированный список: {fill_list}')
    list_numbers = read_file()
    result_list = []
    for i in range(len(fill_list)):
        result_list.append(fill_list[i] * list_numbers[i])
    print(f"Итоговый список: {result_list}")
    return result_list


if __name__ == "__main__":
    main()
