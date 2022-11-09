from random import *
import json

films = []


def save():
    with open("films.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(films, ensure_ascii=False))


def load():
    global films
    with open("films.json", "r", encoding="utf-8") as file:
        films = json.load(file)
    print("Фильмы успешно загружены")
    print(films)


try:
    load()
except FileNotFoundError:
    films = ["Гладиатор", "Кей", "Побег из Шоушенка", "Форест Гамп"]


while True:
    command = input("Введите команду: ")
    match command:
        case "/start":
            print("Бот - фильмотека начал свою работу")
        case "/all":
            print("Список всех фильмов: ")
            print(", ".join(films))
        case "/add":
            film = input("Введите название фильма для добавления: ")
            films.append(film)
            print(f"Фильм - \"{film}\" добавлен в коллекцию!")
        case '/del':
            films_del = input("Введите фильм для удаления: ")
            try:
                films.remove(films_del)
                print(f"Фильм - {films_del} успешно удалён из фильмотеки")
            except ValueError:
                print("Данного фильма нет в фильмотеке")
        case "/random":
            print(f"Случайный фильм для вашего просмотра {choice(films)}!")
        case "/save":
            save()
        case "/load":
            load()
        case "/stop":
            print("Бот завершил свою работу")
            break
        case _:
            print("not command")
