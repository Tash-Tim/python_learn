def film_check(film_list, fil):
    if fil in film_list:
        return True
    return False

films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]
top_list = []
while True:
    print(f'\nВаш ТОП список фильмов: {top_list}')
    film = input('Название фильма: ')
    if film_check(films, film):
        print('Команды: добавить, вставить, удалить')
        com = input('Введите команду: ')
        if com == 'добавить':
            if film_check(top_list, film):
                print('В вашем списке фильм с таким названием уже есть')
            else:
                top_list.append(film)
        if com == 'вставить':
            if film_check(top_list, film):
                print('В вашем списке фильм с таким названием уже есть')
            else:
                f_index = int(input('На какую позицию поставить'))
                top_list.insert(f_index - 1, film)
        if com == 'удалить':
            if len(top_list) == 0:
                print('Ваш список пуст')
            else:
                top_list.remove(film)
    else:
        print(f'Фильм с названием {film} - нет')