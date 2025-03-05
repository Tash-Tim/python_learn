persons_quant = int(input('Кол-во сотрудников: '))
id_list = []

for _ in range(persons_quant):
    person_id = int(input('ID сотрудника: '))
    id_list.append(person_id)

request_id = int(input('Какой ID ищем? '))

# id_status = False
# for i in id_list:
#     if request_id == i:
#         id_status = True
#
# if id_status:
#     print('сотрудник на работе')
# else:
#     print('Сотрудник не работает!')

if request_id in id_list:
    print('сотрудник на работе')
else:
    print('Сотрудник не работает!')