"""
На входе два числа и проверяется: является ли каждое из них квадратом второго
"""


def check_on_square(a, b):
    if a**2 == b:
        return True
    elif b**2 == a:
        return True
    return False


print(check_on_square(3, 3))
