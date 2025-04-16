players_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

a_team = [i_team['name']
          for i_team in players_dict.values()
          if i_team['team'] == 'A' and i_team['status'] == 'Rest']
print(f'Все члены команды А, которые отдыхают: {','.join(a_team)}')

b_team = [i_team['name']
          for i_team in players_dict.values()
          if i_team['team'] == 'B' and i_team['status'] == 'Training']
print(f'Все члены команды B, которые тренируются: {','.join(b_team)}')

c_team = [i_team['name']
          for i_team in players_dict.values()
          if i_team['team'] == 'C' and i_team['status'] == 'Travel']
print(f'Все члены команды C, которые путешествуют: {','.join(c_team)}')