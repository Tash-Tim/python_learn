text = set(input('Введите строку: '))
text_set = set(text)

digit_lst = ''

for i_set in text_set:
    if '0 '< i_set < '9':
        digit_lst += i_set

print(digit_lst)

# digit_lst = []
# for i_set in text:
#     if '0 '< i_set < '9':
#         digit_lst.append(i_set)
#
# print(''.join(digit_lst))
