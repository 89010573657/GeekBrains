"""Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
элемент, второй и предпоследний и т.д.
*Пример:*
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""


def multiplication_num_list(list_m):
    i = 0
    result_list = []
    while i < len(list_m) / 2:
        multiplication = list_m[i]*list_m[len(list_m) - 1 - i]
        result_list.append(multiplication)
        i += 1
    return result_list


def main():
    check_list_1 = [2, 3, 4, 5, 6]
    check_list_2 = [2, 3, 5, 6]
    result_list1 = multiplication_num_list(check_list_1)
    result_list2 = multiplication_num_list(check_list_2)
    print(result_list1)
    print(result_list2)


if __name__ == '__main__':
    main()
