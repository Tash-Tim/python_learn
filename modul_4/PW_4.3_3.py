import random

team1 = [random.randint(50, 80) for _ in range(10)]
team2 = [random.randint(30, 60) for _ in range(10)]
team3 = ['погиб' if team1[i_tm] + team2[i_tm] > 100 else 'выжил' for i_tm in range(10)]

print(f'Урон первого отряда: {team1}')
print(f'Урон второго отряда: {team2}')
print(f'Состояние третьего отряда: {team3}')