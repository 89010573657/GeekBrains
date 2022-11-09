"""
Задача 1. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются
сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""
import json
from random import randint

count_sweets = 2021
end_game = False
count_victory_bot = 0
count_victory_user = 0


def move_bot():
    global count_sweets
    global end_game
    global count_victory_bot
    if count_sweets <= 28:
        count_sweets = 0
        end_game = True
        count_victory_bot += 1
        print("Бот победил")
    else:
        count_take_sweets_bot = count_sweets - 28 * (count_sweets // 28) - 1
        if count_take_sweets_bot == 0:
            count_take_sweets_bot = 1
        elif count_take_sweets_bot == -1:
            count_take_sweets_bot = 27
        print(f"Бот забрал {count_take_sweets_bot} конфет!")
        count_sweets -= count_take_sweets_bot
        print(f"Остаток конфет: {count_sweets}")


def move_user():
    global count_sweets
    global end_game
    global count_victory_user
    count_take_sweets_user = randint(1, 28)
    print(f"Вы забрали {count_take_sweets_user}")
    count_sweets -= count_take_sweets_user
    print(f"Количество оставшихся конфет: {count_sweets}")
    if count_sweets == 0:
        end_game = True
        count_victory_user += 1
        print("Вы победили")


def game_sweets():
    global count_sweets
    print(f'Начальное количество конфет: {count_sweets}')
    draw = randint(0, 1)
    if draw:
        print("Первый ход ваш")
        while count_sweets > 0:
            move_user()
            if not end_game:
                move_bot()
    else:
        print("Первый ход у бота")
        while count_sweets > 0:
            move_bot()
            if not end_game:
                move_user()


def main():
    global count_sweets
    global end_game
    for i in range(100):

        game_sweets()

        count_sweets = 2021
        end_game = False

    print(f"Количество побед бота {count_victory_bot}/100")
    print(f"Количество побед пользователя {count_victory_user}/100")
    with open('result.json', 'w', encoding='utf-8') as fh:
        fh.writelines(json.dumps(f"Количество побед бота {count_victory_bot}/100\n"
                                 f"Количество побед пользователя {count_victory_user}/100", ensure_ascii=False))


if __name__ == "__main__":
    main()
