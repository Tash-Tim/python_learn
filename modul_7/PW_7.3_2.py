import random

def random_sym():
    alfa = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rand_list = [random.choice(alfa) for _ in range(10)]
    return rand_list

def dict_sym(get_list):
    result = {i_ind : i_elem for i_ind, i_elem in enumerate(get_list)}
    return result

frst_lst = random_sym()
scnd_lst = random_sym()

frst_dict = dict_sym(frst_lst)
scnd_dict = dict_sym(scnd_lst)

print('Первый список: {}'.format(frst_lst))
print('Второй список: {}'.format(scnd_lst))

print('\nПервый словарь: {}'.format(frst_dict))
print('Второй словарь: {}'.format(scnd_dict))