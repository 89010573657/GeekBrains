"""
Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех
значений предикат. Количество предикатов генерируется случайным образом от 5 до 11, проверяем это утверждение 10 раз,
с помощью модуля time выводим на экран, сколько времени отработала программа.
"""
from random import *
import time
True_False = [True, False]
start = time.time()
list_predicat = [choice(True_False) for i in range(randint(5, 11))]
print(list_predicat)
res1 = list_predicat[0]
res2 = list_predicat[0]
for i in range(1, len(list_predicat) - 1):
    res1 = res1 or list_predicat[i]
    res2 = res2 and not list_predicat[i]
    print(f'Предикат = {list_predicat[i]}')
    if not res1 == res2:
        print("Утверждение верно", end='\n\n')
    else:
        print("Утверждение неверно")
end = time.time()
time_works = end - start
print(time_works)
