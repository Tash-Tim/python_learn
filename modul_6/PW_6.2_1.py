small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)

for i_prod in big_storage:
    print(f'{i_prod} = {big_storage[i_prod]}')

prod_name = input('\nВведите искомый товар: ')
prod_val = big_storage.get(prod_name)

if prod_val:
    print(f'Товар {prod_name} = {prod_val} шт')
else:
    print(f'Товар "{prod_name}" нет на складе')