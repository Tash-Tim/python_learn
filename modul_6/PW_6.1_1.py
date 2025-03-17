num = int(input('Введите число: '))
num_dict = dict()

for i_num in range(1, num + 1):
    num_dict[i_num] = i_num ** 2

print(num_dict)
