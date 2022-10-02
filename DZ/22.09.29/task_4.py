"""
Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""


def translation_num_10x_in_num_2x(num_10x):
    if num_10x == 0:
        return 0
    num_2x = ''
    while num_10x > 0:
        num_2x = str(num_10x % 2) + num_2x
        num_10x //= 2
    return num_2x


def main():
    check_num_1 = 45
    check_num_2 = 3
    check_num_3 = 2
    result_1 = translation_num_10x_in_num_2x(check_num_1)
    result_2 = translation_num_10x_in_num_2x(check_num_2)
    result_3 = translation_num_10x_in_num_2x(check_num_3)
    print(result_1)
    print(result_2)
    print(result_3)


if __name__ == '__main__':
    main()
