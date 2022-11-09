"""
Задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
*Пример:*
- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3
"""


def number_quarter_coordinates(x, y):  # без учёта x = 0 или y = 0
    if x > 0:
        if y > 0:
            return "Первая четверть"
        else:
            return "Четвёртая четверть"
    else:
        if y > 0:
            return "Вторая четверть"
        else:
            return "Третья четверть"


print(number_quarter_coordinates(1, 1))
print(number_quarter_coordinates(1, -1))
print(number_quarter_coordinates(-1, 1))
print(number_quarter_coordinates(-1, -1))
