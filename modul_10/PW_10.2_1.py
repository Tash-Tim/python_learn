BRUCE_WILLIS = 42
try:
    input_data = input('Введите строку: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except ValueError as exc:
    print('Поймано исключение', exc, type(exc))
except IndexError as exc:
    print('Поймано исключение', exc, type(exc))
except:
    print('Неизвестная ошибка')