info_lst = input(
    'Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): '
).split()
info_dict = dict()

info_dict['Имя'] = info_lst[0]
info_dict['фамилия'] = info_lst[1]
info_dict['город'] = info_lst[2]
info_dict['место учёбы'] = info_lst[3]
info_dict['Оценки'] = []
for i_makr in info_lst[4:]:
    info_dict['Оценки'].append(int(i_makr))

print(info_dict)

for i in info_dict:
    print(f'{i} - {info_dict[i]}')