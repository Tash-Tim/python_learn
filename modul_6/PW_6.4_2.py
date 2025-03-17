import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

nums_1 = set(nums_1)
nums_2 = set(nums_2)
print(f'1-е множество: {nums_1}')
print(f'2-е множество:{nums_2}\n')

i_min_nums_1 = min(nums_1)
nums_1.discard(i_min_nums_1)
i_min_nums_2 = min(nums_2)
nums_2.discard(i_min_nums_2)

print(f'Минимальный элемент 1-го множества: {i_min_nums_1}')
print(f'Минимальный элемент 2-го множества: {i_min_nums_2}\n')

rand_nums_1 = random.randint(100, 200)
nums_1.add(rand_nums_1)
rand_nums_2 = random.randint(100, 200)
nums_2.add(rand_nums_2)
print(f'Случайное число для 1-го множества: {rand_nums_1}')
print(f'Случайное число для 2-го множества: {rand_nums_2}\n')

print(f'Объединение множеств:{nums_1.union(nums_2)}')
print(f'Пересечение множеств: {nums_1.intersection(nums_2)}') # альтернатива intersection = &
print(f'Элементы, входящие в nums_2, но не входящие в nums_1: {nums_2.difference(nums_1)}') # альтернатива difference
# = -
