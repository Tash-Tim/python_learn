cnt_lst = int(input('Кол-во чисел в списке: '))
num_list = []

for i in range(1, cnt_lst + 1):
    print(f'Введите {i} число:', end = ' ')
    number = int(input())
    num_list.append(number)

divider = int(input('Введите делитель: '))
index_sum = 0
print()

for index, j in enumerate(num_list):
    if j % divider == 0:
        print(f'Индекс числа {j}: {index}')
        index_sum += index
print(f'Сумма индексов: {index_sum}')