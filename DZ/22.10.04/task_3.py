"""
задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.
*Пример:*
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

from random import randint


def get_random_coefficient_list(k):
    list_coefficient = [randint(0, 100) for _ in range(k+1)]
    return list_coefficient


def get_formula(multiplier, degree):
    formula = ''
    count = 0
    for i_multiplier in multiplier:
        i_degree = degree - count
        if count == 0 and multiplier == 0:
            i_multiplier = randint(1, 100)
        if i_multiplier == 0:
            continue
        if i_multiplier == 1:
            if i_degree == 0:
                formula += f' +{str(1)}'
            elif i_degree == 1:
                formula += 'x'
            else:
                formula += f' + x^{i_degree}'
        else:
            if i_degree == 0:
                formula += f' + {str(i_multiplier)}'
            elif i_degree == 1:
                formula += f' + {i_multiplier}*x'
            else:
                formula += f' + {i_multiplier}*x^{i_degree}'
        count += 1
    return formula[2:]


def main():
    rand_c = get_random_coefficient_list(6)
    formula = get_formula(rand_c, 6)
    print(formula)
    with open("task_3.txt", 'w') as file:
        file.writelines(formula)


if __name__ == "__main__":
    main()
