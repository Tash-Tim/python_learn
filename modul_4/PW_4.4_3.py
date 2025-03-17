import random

n_list =[random.randint(0, 100) for _ in range(20)]
strt_ind = random.randint(0, 10)
fin_ind = random.randint(11, 20)
new_lst = n_list[strt_ind : fin_ind]

print(f'начальный список {n_list}\n')
print(f'начальный индекс {strt_ind}')
print(f'конечный индекс {fin_ind}')
print(f'\nконечный список {new_lst}')