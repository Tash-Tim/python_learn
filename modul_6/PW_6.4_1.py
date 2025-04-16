sym_set = set(".,;:!?")
text = set(input('Введите строку: '))
sym_sum = text.intersection(sym_set)

print(f'Количество знаков пунктуации: {len(sym_sum)}')