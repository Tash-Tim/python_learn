
import random

def change(nums):
    copy_tuple = list(nums)
    index = random.randint(0, 4)
    value = random.randint(100, 1000)
    copy_tuple[index] = value
    return tuple(copy_tuple), value

my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums)
print(new_nums, rand_val)
new_nums, rand_val_1 = change(new_nums)
rand_val += rand_val_1
print(new_nums, rand_val)