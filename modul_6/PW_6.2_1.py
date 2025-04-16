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

product = input('Введите наименование товара: ').lower()

big_storage.update(small_storage)
price = big_storage.get(product)

if price:
    print(f'Цена товара: {price}')
else:
    print(f'Ошибка! {product} отсутствует на складе')