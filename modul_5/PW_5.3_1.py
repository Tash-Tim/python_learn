word_lst = input('Введите искомые слова через пробел: ').split()
text_lst = input('Введите произведение в одну строку, без знаков препинаний').lower().split()

count = 0
for i_word in word_lst:
    count = text_lst.count(i_word)
    print('Слово {0} в тексте встречается {1} раз'.format(i_word, count))