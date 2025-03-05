str_num = int(input('Введите первое число: '))
fin_num = int(input('Введите второе число: '))

even_lst = [x for x in range(str_num, fin_num + 1) if x % 2 == 0]

print(f'Список четных чисел в диапазоне от {str_num} до {fin_num}: {even_lst}')