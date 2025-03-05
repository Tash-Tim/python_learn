def eql_dstr(tot_part, amnt):
    if tot_part % amnt == 0:
        return True
    print(f'{tot_part} участников невозможно поделить на команды по {amnt} человек!\n')
    return False

part_lst =[]
cnt = 1
while True:
    part_amn = int(input('Кол-во участников: '))
    part_intm = int(input('Кол-во человек в команде: '))
    if eql_dstr(part_amn, part_intm):
        for _ in range(part_amn // part_intm):
            part_lst.append(list(range(cnt, cnt + part_intm)))
            cnt += part_intm
        break
print(f'Общий список команд: {part_lst}')

