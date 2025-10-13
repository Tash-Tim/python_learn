data_file = open('numbers.txt', 'r', encoding='utf-8')
copy_list =[]
for i_line in data_file:
    print(i_line, end='')
    copy_list.append(int(i_line))
copy_sum = str(sum(copy_list))
print(copy_sum)
data_file.close()

copy_file = open('answer.txt.', 'w')
copy_file.write(copy_sum)
copy_file.close()

