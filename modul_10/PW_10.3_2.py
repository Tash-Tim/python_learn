
data_file = open('numbers.txt', 'r', encoding='utf-8')
copy_list =[]

for i_line in data_file:
    print(i_line, end='')
    try:
        copy_list.append(int(i_line))
    except (ValueError, TypeError) as err:
        print('Исключение_1:', err, type(err))
try:
    copy_sum = int(sum(copy_list))
    print(copy_sum)
    data_file.close()
    copy_file = open('answer.txt', 'w')
    copy_file.write(str(copy_sum))
    copy_file.close()
except (ValueError, TypeError) as err:
    print('Исключение_2:', err, type(err))

finally:
    print('numbers.txt закрыто:', data_file.closed)
    print('answer.txt закрыто:', copy_file.closed)
