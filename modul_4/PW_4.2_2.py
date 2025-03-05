text = input('Введите строку: ')
symb = input('Введите дополнительный символ: ')

dbl_wrd = [word * 2 for word in text]
add_sym = [sym + symb for sym in dbl_wrd]

print(f'Список удвоенных символов: {dbl_wrd}')
print(f'Склейка с дополнительным символом: {add_sym}')