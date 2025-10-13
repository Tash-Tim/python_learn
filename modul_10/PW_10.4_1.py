tot_sum = 0
line_cnt = 0
try:
    name_file = open('people.txt', 'r')
    for i_name in name_file:
        name_len = len(i_name)
        line_cnt += 1
        if i_name.endswith('\n'):
            name_len -= 1
        if name_len < 3:
            raise BaseException('Line length {} is less 3'.format(line_cnt))
        tot_sum+= name_len
    name_file.close()
except FileNotFoundError as err:
    print('Exception:', err, type(err))
except BaseException as err:
    print('Exception:', err, type(err))
finally:
    print('Total amount characters is {}'.format(tot_sum))


