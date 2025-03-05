
employees = int(input('Кол-во сотрудников: '))
empl_list = []

for i in range(employees):
    print(f'Зарплата {i + 1} сотрудника: ', end = '')
    salary = int(input())
    empl_list.append(salary)
    if salary == 0:
        empl_list.remove(0)

print(f'\nОсталось сотрудников: {len(empl_list)}')
print(f'Зарплаты: {empl_list}')
print(f'Максимальная зп: {max(empl_list)}')
print(f'Минимальная зп: {min(empl_list)}')