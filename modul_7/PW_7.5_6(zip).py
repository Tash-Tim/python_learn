# a = {'Вася', 'Коля', 'Игорь', 'Катя', 'Саша'}
# b = {30, 40, 27, 18, 19}
#
# print(zip(a, b))
# print(list(zip(a, b)))
# print(dict(zip(a, b)))
# print(set(zip(a, b)))
# print(tuple(zip(a, b)))
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

from itertools import zip_longest
txt = ['Первый', 'четвёртый', 'второй', 'девятый', 'доп', 'лишн']
num = [1, 4, 2, 9]

print(list(zip(txt, num)))
print(dict(zip(txt, num)))
print(set(zip(txt, num)))
print(tuple(zip(txt, num)))

# print()
# txt_num_2 = zip_longest(txt, num, fillvalue=0)
# print(list(zip_longest(txt, num, fillvalue=0)))
# print(dict(zip_longest(txt, num, fillvalue=0)))
# print(set(zip_longest(txt, num, fillvalue=0)))
# print(tuple(zip_longest(txt, num, fillvalue=0)))