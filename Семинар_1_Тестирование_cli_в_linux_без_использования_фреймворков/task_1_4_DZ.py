""- Задание 1.
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в ее выводе
и False в противном случае. Передаваться должна только одна строка, разбиение вывода
использовать не нужно."""


import subprocess


def func(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout
    print(out)
    if result.returncode == 0:
        if text in out:
            return True
        else:
            return False
    else:
        print("FAIL! CODE !=0")


if __name__ == "__main__":
    command1 = "ls -la"
    text1 = "ta"

    print(func(command1, text1))
