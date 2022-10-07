"""
Задача 4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
"""
from task_1 import *


def main():
    num_1 = input_numbers()
    num_2 = input_numbers()
    multiplier_1 = simple_multiplier(num_1)
    multiplier_2 = simple_multiplier(num_2)

    for i in range(len(multiplier_1)):
        if multiplier_1[i] in multiplier_2:
            multiplier_2.remove(multiplier_1[i])

    result = num_1
    for i in multiplier_2:
        result *= i
    print(f'Наименьшее общее кратное чисел {num_1} и {num_2} равняется: {result}')
    with open('task_4.txt', 'w') as file:
        file.write(str(result))


if __name__ == '__main__':
    main()
