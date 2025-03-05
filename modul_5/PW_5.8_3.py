def cmpr_text(text1, text2):
    for i in range(len(text2)):
        temp_text = text2
        temp_text = text2[-i:] + text2[:-i]
        if temp_text == text1:
             return f'Первая строка получается из второй со сдвигом {i}'
    return 'Первую строку нельзя получить из второй с помощью циклического сдвига.'


frst_text = input('Введите первую строку: ')
scnd_text = input('Введите вторую строку: ')
print(cmpr_text(frst_text, scnd_text))


'''
Вариант Skillbox
def shift_detection(first_text, second_text):
    first_text *= 2
    index = first_text.find(second_text)
    if index != -1:
        result = f"Первая строка получается из второй со сдвигом {index}"
    else:
        result = "Первую строку нельзя получить из второй с помощью циклического сдвига."
    return result
    
    
first_text = input('Первая строка: ')
second_text = input('Вторая строка: ')
print(shift_detection(first_text, second_text))
'''