stud_info = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): ').split()
stud_dict = dict()

stud_dict['Имя'] = stud_info[0]
stud_dict['Фамилия'] = stud_info[1]
stud_dict['Город'] = stud_info[2]
stud_dict['Место учёбы'] = stud_info[3]
stud_dict['Оценки'] = ', '.join(stud_info[4:])

for i_info in stud_dict:
    print(f'{i_info} - {stud_dict[i_info]}')
