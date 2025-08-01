"""
Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. Также заполните второй  кортеж
числами от −5 до 0. Объедините два кортежа, создав тем самым третий кортеж. С помощью метода кортежа определите  в
нём количество нулей. Выведите на экран третий кортеж и количество нулей в нём.
"""
import random

def tuple_gen(mi_lm, ma_lm, rng):
    out_tuple = tuple(random.randint(mi_lm, ma_lm) for _ in range(rng))
    return out_tuple

tuple_1 = tuple_gen(0, 5, 10)
tuple_2 = tuple_gen(-5, 0, 10)
tuple_3 = tuple_1.__add__(tuple_2) # 2-й вариант tuple_1 + tuple_2
zero_cnt = tuple_3.count(0)

print(tuple_1)
print(tuple_2)
print(tuple_3)
print(zero_cnt)