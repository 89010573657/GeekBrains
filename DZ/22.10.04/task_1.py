"""
Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""


def input_numbers():
    while True:
        try:
            input_n = int(input("Введите число N: "))
            return input_n
        except ValueError:
            print("Ошибка ввода, нужно ввести натуральное число!")


def simple_multiplier(n):
    if n < 2:
        print("Вводите числа больше 1!!!")
    multiplier = []
    i = 2
    count = 0
    while i != n:
        if n % i == 0:
            multiplier.append(i)
            n //= i
            i = 2
            count += 1
        else:
            i += 1
    multiplier.append(n)
    if count == 0:
        return "Вы ввели простое число"
    return multiplier


def main():
    num = input_numbers()
    print(simple_multiplier(num))


if __name__ == "__main__":
    main()
