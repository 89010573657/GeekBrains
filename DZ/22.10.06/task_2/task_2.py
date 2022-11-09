import json
"""
Задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""

"""
- Кодировку буду производить от 4-х повторений
- Символ экранирования - #
- Количество повторов сразу после сразу после спецсимвола
- Повторяемый элемент за количеством
"""


def get_input_data():
    with open("input_data.txt", "r", encoding="utf-8") as fh:
        data = fh.read()
    return data


def check_count():
    global result_data
    if 0 < count < 4:
        if symbol == "#":
            result_data += '#' + str(count) + symbol
        else:
            result_data += symbol * count
    elif count >= 4:
        result_data += '#' + str(count) + symbol


def coding(input_data):
    global count
    global symbol

    symbol = input_data[0]
    end_cycle = False
    while input_data or not end_cycle:

        if not input_data:
            check_count()
            break

        elif symbol == input_data[0]:
            count += 1

        else:
            check_count()
            symbol = input_data[0]
            count = 1

        input_data = input_data[1:]
    return result_data


def decoding(data):
    result = ""
    while data:
        if data[0] == "#":
            result += int(data[1])*data[2]
            data = data[3:]
        else:
            result += data[0]
            data = data[1:]
    return result


def record_coding_data(data):
    with open("coding.data.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(data, ensure_ascii=False))


count = 0
result_data = ''
i_data = get_input_data()
print(f"Входные данные:\n{i_data}")
symbol = i_data[0]
coding_data = coding(i_data)
print(f"Закодированные данные:\n{coding_data}")
record_coding_data(coding_data)
decoding_data = decoding(coding_data)
print(f"Раскодированные данные:\n"
      f"{decoding_data}")