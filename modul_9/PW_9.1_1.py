import os

file_name = 'Admin.bat'
dir_name = 'access'
rel_path = os.path.join(dir_name, file_name)
abs_path = os.path.abspath(rel_path)
print('Абсолютный путь до файла: {}'.format(abs_path))
print('Относительный путь до файла: {}'.format(rel_path))

