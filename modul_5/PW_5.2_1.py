name = input('Имя: ')
ordr_num = int(input('Номер заказа: '))

messeg = 'Здравствуйте, {clnt_name} Ваш номер заказа: {clnt_ordr_num}. Приятного дня!'.format(
    clnt_name = name,
    clnt_ordr_num = ordr_num
)
print(messeg)