"""Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек и находит
 расстояние между ними в N-мерном пространстве."""
from math import sqrt


while True:
    try:
        n = int(input("Введите мерность пространства: "))
        i = 1
        difference = []
        while n > 0:
            p = float(input(f"Введите координату p для пространства №{i}: "))
            q = float(input(f"Введите координату q для пространства №{i}: "))
            difference.append((p - q)**2)
            i += 1
            n -= 1
        break
    except ValueError:
        print("Ошибка ввода")

result = 0
for i in difference:
    result += i

result = sqrt(result)
print(result)
