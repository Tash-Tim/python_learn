import random

orgn_prc = [random.randint(-20, 20) for _ in range(10)]
copy_prc = orgn_prc[:]
copy_prc = [i_orgn if i_orgn > 0 else 0 for i_orgn in copy_prc]

print(orgn_prc)
print(copy_prc)
print(f'Мы потеряли: {sum(copy_prc) - sum(orgn_prc)}')
