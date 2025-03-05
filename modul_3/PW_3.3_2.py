fst_msg = input('Первое сообщение: ')
snd_msg = input('Второе сообщение: ')

fst_cnt = fst_msg.count('!') + fst_msg.count('?')
snd_cnt = snd_msg.count('!') + snd_msg.count('?')

if fst_cnt > snd_cnt:
    print(f'Третье сообщение: {fst_msg + snd_msg}')
elif fst_cnt < snd_cnt:
    print(f'Третье сообщение: {snd_msg + fst_msg}')
else:
    print('Ой!')