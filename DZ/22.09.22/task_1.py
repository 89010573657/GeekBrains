"""
Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
является ли этот день выходным.
*Пример:*
- 6 -> да
- 7 -> да
- 1 -> нет
"""
weeks = {
    1: "Понедельник",
    2: "Вторник",
    3: "Cреда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}


# def check_days_weeks(numbers):
#     if numbers < 1 or numbers > 7:
#         return "Error - указанное число выходит за пределы количества дней недели"
#     else:
#         return weeks[numbers]
#
#
# """Test"""
# for i in range(9):
#     print(f'{i} - {check_days_weeks(i)}')
#
# """ Усложненный вариант """

def check_days_weeks():

    command = input("Нажмите Enter для продолжения vs Любое значение для закрытия программы: ")
    if command != "":
        print("Всего хорошего")
        return

    while True:
        try:
            day = int(input("Введите число для проверки дня недели: "))
        except ValueError:
            print("Ошибка ввода - вы ввели не натуральное число")
            return check_days_weeks()
        if day < 1 or day > 7:
            print("Error - указанное число выходит за пределы количества дней недели(1-7)")
            return check_days_weeks()
        else:
            print(f'День недели - {weeks[day]}\nВсего хорошего!')
            break


check_days_weeks()
