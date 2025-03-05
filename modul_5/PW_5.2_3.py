count = 0
ip_lst = []
ip_address = '{0}.{1}.{2}.{3}'

while count < 4:
    ip_num = int(input('Введите ip число: '))
    if 0 <= ip_num <= 255:
        ip_lst.append(ip_num)
        count += 1
    else:
        print('Ошибка. Число должно быть больше "0" и меньше "256"')

print(ip_address.format(*ip_lst))