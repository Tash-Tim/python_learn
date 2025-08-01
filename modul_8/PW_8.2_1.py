def fact_func(num):
    if num == 1:
        return 1
    fact_1 = fact_func(num - 1)
    return num * fact_1

set_num = int(input('Введите число: '))
print('{:e}'.format(fact_func(set_num)))