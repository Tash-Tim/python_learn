def  code_mes(text_lst, num):
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    new_word = ''.join([alpha[(alpha.index(i_elem) + num) % len(alpha)]
                if i_elem.isalpha() else i_elem
                for i_text in text_lst for i_elem in i_text])

    return new_word


mess_lst = input('Введите сообщение: ').lower()
shift = int(input('Введите сдвиг: '))
print(f'Зашифрованное сообщение: {code_mes(mess_lst, shift)}')