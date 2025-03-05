wrd_lst = []
lst_amt = int(input('Длина списка: '))

for i in range(lst_amt):
    print(f'Введите {i + 1} слово: ', end = '')
    word = input()
    cnt = 0
    wrd_lst.append([word, cnt])

print(wrd_lst)

wrd_txt = input('введите слово из текста: ')

while wrd_txt != 'end':
    for index in range(lst_amt):
        if wrd_lst[index][0] == wrd_txt:
           wrd_lst[index][1] += 1
    wrd_txt = input('введите слово из текста: ')

for i in range(lst_amt):
    print(f'Слово {wrd_lst[i][0]} встречается {wrd_lst[i][1]} раз')