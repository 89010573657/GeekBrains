"""
36. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
Порядок элементов менять нельзя
"""
import json


with open('input_data.json', 'r', encoding='utf-8') as fh:
    input_data = json.load(fh)


result_list = []
for i, element in enumerate(input_data):
    if element not in result_list and element == max(input_data[:i+1]):
        result_list.append(element)
print(result_list)

file = open('result.json', 'w', encoding='utf-8')
file.writelines(json.dumps(result_list, ensure_ascii=False))
file.close()
