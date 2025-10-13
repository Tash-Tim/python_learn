to_file = None
try:
    user_insert = int(input('Введите строку: '))
    try:
        to_file = open('10_3.1_.txt', 'w', encoding='utf-8')
        to_file.write(user_insert)
        to_file.close()
    except (FileNotFoundError, TypeError, ValueError) as error:
        print('Поймано исключение:', error, type(error))
    else:
        print('Внутренняя программа выполнена успешно!')
except ValueError as error:
    print('Поймано исключение "user_insert":', error, type(error))
else:
    print('Внешняя программа выполнена успешно!')
finally:
    to_file.close()
    print(to_file.closed)
