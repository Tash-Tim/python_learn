file = open('D:/03_ Py_Project/task/group_1.txt', 'r', encoding='utf-8')
summa = 0
for i_line in file:
    info = i_line.split()
    summa += int(info[2])
file.close()
file = open('D:/03_ Py_Project/task/group_1.txt', 'r', encoding='utf-8')
diff = 0
for i_line in file:
    info = i_line.split()
    diff -= int(info[2])
file.close()
file = open('D:/03_ Py_Project/task/Additional_info/group_2.txt', 'r', encoding='utf-8')
compose = 1
for i_line in file:
    info = i_line.split()
    compose *= int(info[2])
print(summa)
print(diff)
print(compose)