"""
Задача 3. Реализуйте алгоритм перемешивания списка. Список размерностью 10 задается случайными целыми числами,
выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!
"""
from random import randint


def new_list_length_10():
    new_list = []
    for i in range(10):
        new_list.append(randint(0, 99))
    return new_list


def mixing_list(list):
    count_mix = randint(3, 9)
    while count_mix > 0:
        swap_index_one = randint(0, len(list) - 1)
        swap_index_two = randint(0, len(list) - 1)
        print(f'Замена: число - {list[swap_index_one]} c id({swap_index_one}), на число -'
              f' {list[swap_index_two]} c id({swap_index_one})')
        swap = list[swap_index_one]
        list[swap_index_one] = list[swap_index_two]
        list[swap_index_two] = swap
        print(f'Получившийся список:'
              f'\n{list}')
        count_mix -= 1
    return list


new_list = new_list_length_10()
print(f'Изначальный список:\n{new_list}')
mixing_list(new_list)
