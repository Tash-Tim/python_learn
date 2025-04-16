contact_dict = dict()
while True:
    print('Текущие контакты на телефоне:')
    if contact_dict:
        for i_cont in contact_dict:
            print(i_cont, contact_dict[i_cont])
    else:
        print('<Пусто>')

    name = input('\nВведите имя: ')
    if name == '':
        break
    elif name in contact_dict:
        print(f'Внимание! имя {name} уже есть в списке\n')
    else:
        number = int(input('Введите номер телефона: '))
        contact_dict[name] = number