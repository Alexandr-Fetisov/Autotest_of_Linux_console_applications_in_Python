"""- Задание 2. (повышенной сложности).

Доработать функцию из предыдущего задания таким образом,
чтобы у нее появился дополнительный режим работы, в котором вывод разбивается на слова
с удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string).
В этом режиме должно проверяться наличие слова в выводе."""

import subprocess
import re


def func(command, text, task=1):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    out = result.stdout

    if result.returncode == 0:
        if task == 1:
            print(out)
        elif  task == 2:
            out = re.sub(r'[^\w\s]', ' ', out)
            print(out)
        else:
            print("такого задания нет")
            raise ValueError

        if text in out:
            return True
        else:
            return False
    else:
        print("FAIL! CODE !=0")


if __name__ == "__main__":
    command1 = "ls -la"
    text1 = "ta"
    task2 = 2
    print(func(command1, text1, task2))
