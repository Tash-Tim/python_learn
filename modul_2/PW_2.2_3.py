dog_cnt = int(input('Количество собак: '))
points_list = []

for i in range(1, dog_cnt + 1):
    print(f'Введите очко {i}-й собаки:', end = ' ')
    point = int(input())
    points_list.append(point)
print(f'\nСписок очков до: {points_list}')

max_point = points_list[0]
min_point = points_list[0]
max_index = 0
min_index = 0

for index, j in enumerate(points_list):
    if j > max_point:
        max_point = j
        max_index = index
    if j < min_point:
        min_point = j
        min_index = index

print(f'\nМаксимальное число в списке: {max_point}')
print(f'Минимальное число в списке: {min_point}')

points_list[max_index], points_list[min_index] = points_list[min_index], points_list[max_index]

print(f'\nСписок очков после: {points_list}')