text = input('Введите строку: ')

cnt_up = len([i_txt for i_txt in text if i_txt.isupper()])
cnt_lw = len([i_txt for i_txt in text if i_txt.lower()])

if cnt_up > cnt_lw:
    print(f'Результат: {text.upper()}')
else:
    print(f'Результат: {text.lower()}')