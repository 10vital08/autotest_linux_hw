"""
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и
False в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""

import subprocess


def find_text(comand, text_find):
    result = subprocess.run(comand, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    res = result.stdout.split()

    print(result)
    print(res)

    if text_find in res:
        return True
    else:
        return False


if find_text("cat ./test_1.txt", "vital"):
    print("True")
else:
    print("False")
