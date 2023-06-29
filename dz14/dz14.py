"""
ЗАДАНИЕ 1
Создать 3 папки с именами folder1, folder2, folder3 соответственно,
создать в каждой папке файл random_number.txt и записать в него случайное число.

ПОДХОДЯЩИЕ ПРИМЕРЫ:

1.  'Создаётся 3 разные папки [folder1, folder2, folder3].
     В каждой из этих папок создаётся отдельный текстовый файл с названием 'random_number.txt'
     В который записывается случайно сгенерированное число'

НЕПОДХОДЯЩИЕ ПРИМЕРЫ:

1.  'Папки создаются друг в друге без возвращения к исходному пути
     В остальном все работает корректно'

2.  'Все работает корректно, но во всех .txt файлах записывается одинаковое число'

"""

import os
from random import randint as r

dir_list = ['folder1', 'folder2', 'folder3']


def creater(dir_list: list):
    for name_dir in dir_list:
        random_num = r(1, 100)
        print(random_num)
        os.mkdir(f'{name_dir}')
        os.chdir(f'{name_dir}')
        with open('random_number.txt', 'w+') as f:
            f.write(str(random_num))
            os.chdir('../')
            print(os.getcwd())


creater(dir_list)
