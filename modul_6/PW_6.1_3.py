phone_book_dict = dict()

while True:
    print(f'Текущий контакт на телефоне:')

    if phone_book_dict:
        for i_cont in phone_book_dict:
            print(f'{i_cont} {phone_book_dict[i_cont]}')
    else:
        print('<Пусто>')

    add_name = input('\nВведите имя: ')

    if add_name == '':
        break
    elif add_name not in phone_book_dict:
        add_num = int(input('Введите номер телефона: '))
        phone_book_dict[add_name] = add_num
        print()
    else:
        print(f'Ошибка. Пользователь с именем {add_name} уже есть в списке\n')

