punk_sym = {'.', ',', ';', ':', '!', '?'}
text = set(input('Введите строку: '))
punk_sym_text = text & punk_sym
print(f'Знаков пунктуации в строке: {punk_sym_text}')
print(f'Количество знаков пунктуации: {len(punk_sym_text)}')