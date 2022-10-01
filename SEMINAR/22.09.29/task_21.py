"""Определить, позицию второго вхождения строки в списке либо сообщить, что её нет. Примеры:
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1
"""


def check_index_two_entry(list_string, string):
    count = 0
    j = 0
    for i in list_string:
        if string == i:
            count += 1
        if count == 2:
            return f'index второго вхождения: {j}'
        j += 1
    return -1


def main():
    list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
    string1 = "qwe"
    list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
    string2 = "йцу"
    list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
    string3 = "йцу"
    list4 = ["123", "234", 123, "567"]
    string4 = "123"
    list5 = []
    string5 = "123"
    print(check_index_two_entry(list1, string1))
    print(check_index_two_entry(list2, string2))
    print(check_index_two_entry(list3, string3))
    print(check_index_two_entry(list4, string4))
    print(check_index_two_entry(list5, string5))


if __name__ == '__main__':
    main()
