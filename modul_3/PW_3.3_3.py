pack = []
decode = []
bad_pack = 0

pack_amt = int(input('Кол-во пакетов: '))

for i_pack in range(pack_amt):
    print(f'\nПакет номер: {i_pack + 1}')
    for i_bit in range(4):
        print(f'{i_bit + 1} бит: ', end = '')
        bit = int(input())
        pack.append(bit)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        bad_pack += 1
        print('Много ошибок в пакете.')

    pack.clear()

print(f'Полученное сообщение: {decode}')
print(f'Кол-во ошибок в сообщении: {decode.count(-1)}')
print(f'Кол-во потерянных пакетов: {bad_pack}')