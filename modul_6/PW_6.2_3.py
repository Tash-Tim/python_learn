def hist_fun(string):
    hist_dict = dict()
    for i_sym in string:
        if i_sym in hist_dict:
            hist_dict[i_sym] += 1
        else:
            hist_dict[i_sym] = 1
    return hist_dict

text = input('Введите текст: ').lower()
hist = hist_fun(text)

for i_hist in sorted(hist.keys()):
    print(f'{i_hist} : {hist[i_hist]}')
print(f'Максимальная частота: {max(hist.values())}')