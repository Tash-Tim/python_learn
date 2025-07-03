tilda_text = input('Введите текст со знаком ~: ')

for i_ind, i_elim in enumerate(tilda_text):
    if i_elim == '~':
        print(i_ind, end = ' ')