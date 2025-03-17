from tkinter.font import names

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

a_team = [i_ateam['name']
    for i_ateam in players_dict.values()
          if i_ateam['status'] == 'Rest']

b_team = [i_bteam['name']
    for i_bteam in players_dict.values()
          if i_bteam['status'] == 'Training']

c_team = [i_cteam['name']
    for i_cteam in players_dict.values()
          if i_cteam['status'] == 'Travel']

print('Члены команды А, которые отдыхают: {}'.format(a_team))
print('Члены команды В, которые тренируются: {}'.format(b_team))
print('Члены команды C, которые путешествуют: {}'.format(c_team))