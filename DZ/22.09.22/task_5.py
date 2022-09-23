"""Задача 5 VERY HARD SORT необязательная
Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы
по возрастанию слева направо и сверху вниз.
Например, задан массив:
1 4 7 2
5 9 10 3
После сортировки
1 2 3 4
5 7 9 10
"""
from random import randint


def create_array(height, width):  # создание, заполнение и вывод двумерного массива
    array_2d = []
    for i in range(height):
        array_1d = []
        for j in range(width):
            numbers = randint(0, 99)
            array_1d.append(numbers)
            if numbers > 9:
                print(array_1d[j], end=" ")
            else:
                print(array_1d[j], end="  ")
        array_2d.append(array_1d)
        print()
    return array_2d


def sort_array(array_2d, height, width):  # сортировка двумерного массива через одномерный
    result_array = []
    array_1d_sort = []

    for i in range(height):
        for j in range(width):
            array_1d_sort.append(array_2d[i][j])

    print(f'Все значения из двумерного массива переведенные в одномерный\n{array_1d_sort}')
    array_1d_sort.sort()
    print(f'Упорядоченный одномерный массив:\n{array_1d_sort}')

    count = 0
    print("Упорядоченный массив")
    for i in range(height):
        array_1d = []
        for j in range(width):
            array_1d.append(array_1d_sort[count])
            count += 1
        result_array.append(array_1d)
        print(*array_1d)


height = randint(2, 10)
width = randint(2, 10)
print(f"Рандомные значение двумерного массива: высота - {height}, ширина - {width}!")
print("Созданный двумерный массив:")
new_array = create_array(height, width)
sort_array(new_array, height, width)
