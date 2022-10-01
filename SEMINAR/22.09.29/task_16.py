"""
16. Задайте список из n чисел последовательности (1 + 1/n)^n  и выведите на экран их сумму.
"""


def get_n():
    try:
        input_n = int(input("Введите N: "))
        return input_n
    except ValueError:
        print("Ошибка ввода")


def get_result_formula(i):
    return (1+1/i)**i


def fill_list(length):
    f_list = []
    for i in range(1, length + 1):
        f_list.append(get_result_formula(i))
    return f_list


n = get_n()
result_list = fill_list(n)
print(result_list)
print(sum(result_list))
