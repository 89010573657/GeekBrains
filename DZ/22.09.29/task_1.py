"""Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
*Пример:*
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""


from random import randint


def random_length_list():
    length_list = randint(3, 99)
    return length_list


def fill_new_list(length):
    new_list = []
    for i in range(length):
        new_list.append(randint(0, 1000))
    return new_list


def counting_sum_odd_index_elements(list):
    i = 1
    sum_element = 0
    while i < len(list):
        sum_element += list[i]
        i += 2
    return sum_element


def main():
    length = random_length_list()
    new_list = fill_new_list(length)
    print(new_list)
    result = counting_sum_odd_index_elements(new_list)
    print(f'Сумма элементов на нечётных позициях: {result}')
    return result


if __name__ == '__main__':
    main()
