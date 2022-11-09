"""
Задача №34: Даны два файла, в каждом из которых находится запись многочлена.
Сформировать файл, содержащий сумму многочленов
"""
import json

with open('task_34_formula_1.txt', 'r') as file:
    str_formula_1 = file.read()
file = open("task_34_formula_2.txt", "r")
str_formula_2 = file.read()
file.close()


def get_list_formula(str_formula):
    list_formula = str_formula.split(" + ")
    return list_formula


def get_dict_coefficient(list_formula):
    dict_formula = {}
    for i in list_formula:
        if i.count("*x^"):
            value, key = map(int, i.split("*x^"))
            dict_formula[key] = value
        elif i.count("x^"):
            key = int(i[i.index("^")+1:])
            dict_formula[key] = 1
        elif i.count("*x"):
            value = int(i[:i.index("*")])
            dict_formula[1] = value
        elif i.count("x"):
            dict_formula[1] = 1
        else:
            dict_formula[0] = int(i)
    return dict_formula


def get_sum_coefficient(dict_formula_1, dict_formula_2):
    result_dict_formula = {}
    for i in dict_formula_1:
        if i in dict_formula_2:
            result_dict_formula[i] = dict_formula_1[i] + dict_formula_2[i]
            del dict_formula_2[i]
        else:
            result_dict_formula[i] = dict_formula_1[i]
    result_dict_formula.update(dict_formula_2)
    return result_dict_formula


def get_result_list_formula(r_dict_formula):
    r_list_formula = []
    for key, value in r_dict_formula.items():
        if key > 1:
            r_list_formula.append(str(value)+"*x^"+str(key))
        elif key == 1:
            if value > 1:
                r_list_formula.append((str(value) + "*x"))
            else:
                r_list_formula.append('x')
        else:
            r_list_formula.append(str(value))
    return r_list_formula


def main():

    list_formula_1 = get_list_formula(str_formula_1)
    list_formula_2 = get_list_formula(str_formula_2)

    dict_formula_1 = get_dict_coefficient(list_formula_1)
    dict_formula_2 = get_dict_coefficient(list_formula_2)

    print("Коэффициенты первой формулы:", dict_formula_1, "Коэффициенты второй формулы:", dict_formula_2, sep="\n")

    result_dict_formula = get_sum_coefficient(dict_formula_1, dict_formula_2)
    print(f'Коэффициенты результирующей формулы:\n{result_dict_formula}')

    result_list_formula = get_result_list_formula(result_dict_formula)
    print(result_list_formula)
    result = " + ".join(result_list_formula)
    print(f"Итоговая формула:\n{result}")

    with open('result.txt', 'w', encoding='utf-8') as fh:
        fh.write(f'Итогова формула: {result}')

    with open('result.json', 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(result))


if __name__ == "__main__":
    main()
