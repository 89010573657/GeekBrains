"""
Задача5 HARD необязательная.
Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры), причем чтобы
количество элементов было четное. Вывести на экран красивенько таблицей. Перемешать случайным образом элементы
массива, причем чтобы каждый гарантированно переместился на другое место и выполнить это за m*n / 2 итераций.
То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран
как таблицу.
"""
from random import randint


def input_size_array():  # запрашивает и передаёт размеры массива в кортеже
    while True:
        try:
            height = int(input("Введите высоту массива - чётное число: "))
            if height % 2 != 0:
                continue
            width = int(input("Введите ширину массива: "))

            size_array = (height, width)
            return size_array
        except ValueError:
            print("Ошибка ввода, введите целые числа")


def fill_new_array_random_numbers(height, width):  # заполняет массив случайными числами и передаёт его
    array = []
    for i in range(height):
        array_width = []
        for j in range(width):
            array_width.append(randint(0, 99))
        array.append(array_width)
    return array


def output_array_2x(array):  # выводит в консоль двумерный массив
    for i in array:
        for j in i:
            if j < 10:
                print(f'{j:2}', end=' ')
            else:
                print(j, end=" ")
        print()


def mixing_array(array):  # перемешивает двумерный массив
    already_mixing = []  # список для запоминаний перемешанных строк
    while len(array) != len(already_mixing):
        while True:
            numbers_swap_width_one_random = randint(0, len(array) - 1)
            numbers_swap_width_two_random = randint(0, len(array) - 1)

            if numbers_swap_width_one_random != numbers_swap_width_two_random and \
                    numbers_swap_width_one_random not in already_mixing and \
                    numbers_swap_width_two_random not in already_mixing:
                break

        swap = array[numbers_swap_width_one_random]
        array[numbers_swap_width_one_random] = array[numbers_swap_width_two_random]
        array[numbers_swap_width_two_random] = swap

        already_mixing.append(numbers_swap_width_one_random)
        already_mixing.append(numbers_swap_width_two_random)

    return array


def main():
    size_array = input_size_array()
    height = size_array[0]
    width = size_array[1]
    new_array = fill_new_array_random_numbers(height, width)
    print("Сформированный массив")
    output_array_2x(new_array)
    mix_array = mixing_array(new_array)
    print("Перемешанный массив")
    output_array_2x(mix_array)


if __name__ == '__main__':
    main()
