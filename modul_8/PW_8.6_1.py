
def file_proces(question,
                complaint='Пожалуйста, введите да или нет',
                retries = 4):
    while True:
        answer = input(question).lower()
        if answer == 'да':
            return 1
        if answer == 'нет':
            return 0
        retries -= 1
        if retries == 0:
            print('Количество попыток истекло!')
            break
        print(complaint)
        print('Количество повторов', retries)

file_proces('Вы действительно хотите выйти? ')
file_proces('Удалить файл? ', 'Так удалить или нет? ')
file_proces('Записать файл? ', retries=2)