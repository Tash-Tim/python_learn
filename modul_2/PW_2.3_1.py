texts = input('Введите строку: ')
#sym_index = 0
replace_cnt = 0

sym_list = list(texts)

# for i in sym_list:
#     if i ==':':
#         sym_list[sym_index] = ';'
#         replace_cnt +=1
#     sym_index += 1

for index, i in enumerate(sym_list):
    if i == ':':
        sym_list[index] = ';'
        replace_cnt +=1

print('Исправленная строка: ', end = '')
for j in sym_list:
    print(j, end = '')

print(f'\nКол-во замен: {replace_cnt}')