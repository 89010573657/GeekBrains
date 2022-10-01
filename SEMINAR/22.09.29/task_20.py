"""
Определить, присутствует ли в заданном списке строк, некоторое число
"""

def presence(numbers, list):
    for i in list:
        if str(numbers) in str(i):
            return list.index(i)
    return -1


def main():
    list = [42, '345', 48.2, '9', True]
    try:
        numbers = int(input("Введите число: "))
        print(presence(numbers, list))
    except ValueError:
        print("Ошибка ввода")


if __name__ == '__main__':
    main()