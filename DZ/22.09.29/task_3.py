"""
Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
и минимальным значением дробной части элементов.
*Пример:*
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
import sys

def search_max_fractional_part(list):
    max_fractional_part = 0
    for i in list:
        if max_fractional_part < i - i // 1:
            max_fractional_part = i - i // 1
    return max_fractional_part


def search_min_fractional_part(list):
    min_fractional_part = sys.maxsize
    for i in list:
        if (min_fractional_part > i - i // 1) and (i - i // 1 != 0):
            min_fractional_part = i - i // 1
    return min_fractional_part


def main():
    check_list = [1.1, 1.2, 3.1, 5, 10.01]
    max_fractional_part = search_max_fractional_part(check_list)
    min_fractional_part = search_min_fractional_part(check_list)
    result = max_fractional_part - min_fractional_part
    print(result)
    return result


if __name__ == "__main__":
    main()

