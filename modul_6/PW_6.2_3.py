def hist_fun(string : str) -> dict:
    text_dict = dict()
    for i_str in string:
        if i_str not in text_dict:
            text_dict[i_str] = 1
        else:
            text_dict[i_str] += 1
    return text_dict

text = input('Введите текст: ').lower()
hist = hist_fun(text)

for i_hist in sorted(hist.keys()):
    print(i_hist, '=', hist[i_hist])

print(f'Максимальная частота: {max(hist.values())}')

