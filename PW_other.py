# text = 'Привет! меня зовут Темур'
# temp_list = ''
# text_list = []
#
# # формирует список со вложенным списком
# for i in text + ' ':
#     if i != ' ':
#         temp_list += i
#     else:
#         text_list.append(list(temp_list))
#         temp_list = ''
#
# print(text_list)
#
# # выводит на экран список в виде матрицы
# for i_list in text_list:
#     for j in i_list:
#         print(j, end = '')
#     print()


"""
не удалять верхний код
"""
import copy
from traceback import print_tb

# rev_dbl_num = [num * 2 for num in range(10 , 1 , -1) if num % 2 == 0]
# print(rev_dbl_num)

# words = ['hello', 'hey', 'goodbye', 'guitar', 'piano']
# new_words = [word + '.' for word in words if len(word) <= 5]
# print(new_words)

# a = [1, 4, 6, 10, 2, 3]
# a[:5] = [1, 2, 3]
# print(a)

# start = -2
# end =  2
# step =  -1
#
# if start < end:
#     start, end = end, start
#
# for x in range(start, end - 1, step):
#     y = (x ** 3 + 2 * x ** 2 - 4 * x + 1)
#     print(f'В точке {x} функция равна {y}')

'___________________________________________________________'
# a = {'Вася', 'Коля', 'Игорь', 'Катя', 'Саша'}
# b = {30, 40, 27, 18, 19}
#
# print(zip(a, b))
# print(list(zip(a, b)))
# print(dict(zip(a, b)))
# print(set(zip(a, b)))
# print(tuple(zip(a, b)))
#
# print()
#
# for i in zip(a, b):
#     print(i, end=' ')
# print()
#
# for j, k in zip(a, b):
#     print(j, k, end=' ')
# print()
#
# d = {name : age
#      for name, age in zip(a,b,)}
# print(d)
#
# e = [pip
#      for pip in zip(a,b,)]
# print(e)

'___________________________________________________________'
# a = ('Саша', 18), ('Катя', 19), ('Вася', 27), ('Коля', 30), ('Игорь', 40)
# print(dict(a))

'___________________________________________________________'
#
# tuple = (1, 2, 3)         # Есть неизменяемый объект (кстати, попробуйте потом повторить этот код с изменяемымобъектом)
# hash_value = hash(tuple)            # Применим к этому объекту функцию hash
# print(hash_value, type(hash_value))                   # Проверим, что получилось (бессмысленный набор чисел)
# hash_value_2 = hash(tuple)          # Попробуем ещё раз
# print(hash_value_2, type(hash_value_2))                 # Опять набор чисел
# print(hash_value == hash_value_2)   # И он в точности равен первому

# def simple_hash(input_string): # На вход получаем строку
#     hash_value = 0
#     for char in input_string: # Запускаем цикл по символам строки
#         hash_value += ord(char) # Суммируем код каждого символа
#     return hash_value # На выходе получаем сумму — некое числовое значение
#
# print(simple_hash('python'))
# print(simple_hash('pythonik'))

# import sys
#
# test_list = [1, 2, 3]
# test_tuple = (1, 2, 3)
#
# # print(sys.getsizeof((test_list)))
# # print(sys.getsizeof((test_tuple)))
# print(sys.version)

# import os
#
# user_dir = os.path.abspath(os.sep)
# dir_files = os.listdir(user_dir)
# print('Сейчас в этой директории:', user_dir, '\n')
# for i in dir_files:
#     print(os.path.join(user_dir, i))

class Friend:
    name = 'CommaName'
    surname = 'CommaSur'
    frnd_cnt = 0
    friends = []

    def print_info(self):
        print(f'{self.frnd_cnt} friend Name: {self.name}, Surname: {self.surname}; Frends List: {self.friends}')

    def add_friend(self, name = 'CommaName', surname = 'CommSur'):
        self.name = name
        self.surname = surname
        Friend.frnd_cnt += 1
        self.friends.append(name + ' ' + surname)
        self.print_info()

frnd_1 = Friend()
frnd_2 = Friend()

frnd_1.print_info()
frnd_2.print_info()

print(frnd_1.friends)