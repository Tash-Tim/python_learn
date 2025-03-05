strt_num = int(input('Левая граница: '))
fin_num = int(input('Правая граница: '))

cub_list = [num ** 3 for num in range(strt_num, fin_num + 1)]
sqr_list = [num ** 2 for num in range(strt_num, fin_num + 1)]

print(f'Список кубов чисел в диапазоне от {strt_num} до {fin_num}: {cub_list}')
print(f'Список квадратов чисел в диапазоне от {strt_num} до {fin_num}: {sqr_list}')