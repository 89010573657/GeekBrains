"""
Задача №38: Напишите программу, удаляющую из текста все слова, содержащие "абв".
Пример:
Входные данные: 'ываабв лповап абвцукв алоабвабв ываываыв'
Выходные данные: 'лповап ываываыв'
"""
import json


def get_load_input_data():
    with open('input_data.json', 'r', encoding='utf-8') as fh:
        in_data = json.load(fh)
    return in_data


def record_result_txt_and_json(data):
    with open("result.txt", "w", encoding='utf-8') as fh:
        fh.writelines(data)
    with open("result.json", "w", encoding="utf-8") as fh:
        fh.writelines(json.dumps(data, ensure_ascii=False))


def del_words(data):
    result_data = " ".join([i for i in data.split() if 'абв' not in i])
    return result_data


def main():
    input_data = get_load_input_data()
    print(f"Входные данные:\n{input_data}\n")
    result = del_words(input_data)
    print(f"Результат:\n{result}")
    record_result_txt_and_json(result)


if __name__ == "__main__":
    main()
