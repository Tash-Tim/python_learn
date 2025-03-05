def text_coding(text):
    count, result = 0, ''
    for index, symbol in enumerate(text):
        count += 1
        if index == len(text) - 1 or symbol != text[index + 1]:
            result += f'{symbol}{count}'
            count = 0
    return result


user_text = input('Введите строку: ')
print(f'Закодированная строка: {text_coding(user_text)}')