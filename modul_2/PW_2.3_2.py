text = input('Введите строку: ')
symbol_num = int(input('Номер символа: '))

text_list = list(text)

print(f'\nСимвол слева: {text_list[symbol_num - 2]}')
print(f'Символ слева: {text_list[symbol_num]}')

if text_list[symbol_num - 2] == text_list[symbol_num - 1] and text_list[symbol_num] == text_list[symbol_num - 1]:
    print(f'\nЕсть два таких же символов')
elif text_list[symbol_num - 2] == text_list[symbol_num - 1] or text_list[symbol_num] == text_list[symbol_num - 1]:
    print(f'\nЕсть ровно один такой же символ')
else:
    print(f'\nТаких же символов нет')