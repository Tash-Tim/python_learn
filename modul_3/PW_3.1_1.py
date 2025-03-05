# разбор HW из модуля 15, задача 8_sort
# вариант от Skillbox
def sort_fun(my_list):
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[j] < my_list[i]:
                my_list[j], my_list[i] = my_list[i], my_list[j]

num_list = [1, 4, -3, 0, 10]
sort_fun(num_list)
print(num_list)