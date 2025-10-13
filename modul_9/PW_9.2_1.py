import os

obj_path = input('Путь: ')

if os.path.isdir(obj_path):
    print('Это директория (папка)')
elif os.path.isfile(obj_path):
    print('Это файл')
    print('Размер файла:', os.path.getsize(obj_path), 'байт')
elif os.path.islink(obj_path):
    print('Это ссылка')
else:
    print('Указанного пути не существует')