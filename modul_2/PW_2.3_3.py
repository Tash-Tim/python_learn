words_list = []
cnt_list =[0, 0, 0]

for i in range(3):
    print(f'Введите {i + 1}-e слово: ', end = '')
    word = input()
    words_list.append(word)

text = input('\nСлово из текста: ')
while text != 'end':
    for index in range(3):
        if words_list[index] == text:
            cnt_list[index] += 1
    text = input('Слово из текста: ')

print('\nПодсчёт слов в тексте:')
for j in range(3):
    print(f'{words_list[j]} : {cnt_list[j]}')