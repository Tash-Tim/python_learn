file_add = input('Путь к файлу: ')
disk_chk = input('На каком диске должен лежать файл: ')
file_ext = input('Требуемое расширение файла: ')

if not file_add.startswith(disk_chk):
    print('Указан неверный диск')
elif not file_add.endswith(file_ext):
    print('Указан неверное расширение файла')
else:
    print('Путь корректен')