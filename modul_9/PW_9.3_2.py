import os
import random

def find_dir(direct, target):
    dir_list = []
    print('\nИщу в директории:', direct)
    for i_elem in os.listdir(direct):
        path = os.path.join(direct, i_elem)
        if i_elem in target:
            print(f'   Файл {i_elem} найдет. Путь: {path}')
            dir_list.append(path)
        elif os.path.isdir(path):
            result = (find_dir(path, target))
            if result:
                dir_list.extend(result)
    return dir_list


def open_file(get_path):
    print(f'\nОткрыть файл {get_path}')
    file = open(get_path, 'r', encoding='utf-8')
    for line in file:
        print('   ',line, end='')
    file.close()


loc_dir = os.path.abspath(os.path.join('..', '..', 'Test_dir'))
find_file = ('Data_932.txt', 'Data_932_dbl.txt')
path_list = find_dir(loc_dir, find_file)
open_file(random.choice(path_list))

