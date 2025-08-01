site = {
    'html': {
        'head': {'title': 'Мой сайт'},
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'}
    }
}

def find_key(struct, key):
    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None

    return result


set_key = input('Введите искомый кюч: ')
value = find_key(site, set_key)
if value:
    print('Значение: {}'.format(value))
else:
    print('Такого ключа нет в структуре')