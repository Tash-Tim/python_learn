while True:
    sampl = input('Введите шаблон поздравления с конструкцией {name} и {age}: ')
    if '{name}' in sampl and '{age}' in sampl:
        break

name_lst = input('Список ФИ людей через запятую: ').split(', ')
birth_age = input('Возраст людей через пробел: ')
age_lst = [int(i_age) for i_age in birth_age.split()]

print()
for i_name in range(len(name_lst)):
    print(sampl.format(name = name_lst[i_name], age = age_lst[i_name]))

birth_pip_lst = [' '.join([name_lst[i_man], str(age_lst[i_man])])
    for i_man in range(len(name_lst))
]
birth_pip = ', '.join(birth_pip_lst)

print(f'\nИменинники: {birth_pip}')

