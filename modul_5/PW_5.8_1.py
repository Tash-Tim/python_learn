menu_str = 'утиное филе;фланк-стейк;банановый пирог;плов'
new_menu_str = ', '.join(menu_str.split(';')).title()

print('Доступное меню: {}'.format(menu_str))
print('На данный момент в меню есть: {}'.format(new_menu_str))

'''
Решение Skilbox

def nice_view(text):
    text = ", ".join(text.split(';'))
    return text.title()
site_menu = input('Введите доступное меню: ')
print('Доступное меню:', site_menu)
print('На данный момент в меню есть:', nice_view(site_menu))
'''