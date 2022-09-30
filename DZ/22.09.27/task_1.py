"""Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
Через строку нельзя решать.
*Пример:*
- 6782 -> 23
- 0,56 -> 11"""


def sum_numbers(num):

    while num % 10 > 0.0000000001:
        num *= 10

    result = 0
    num = int(num)
    while num > 0:
        result += num % 10
        num = num // 10
    return result


print(sum_numbers(10341.3))
