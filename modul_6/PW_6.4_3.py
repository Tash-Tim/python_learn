text = set(input('Введите строку: '))
result = text.intersection(set('0123456789'))

print(f'Различные цифры строки: {''.join(sorted(result))}')