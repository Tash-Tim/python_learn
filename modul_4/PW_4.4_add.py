import random

def polindrom(num_list):
    new_list = num_list[:: -1]
    if new_list == num_list:
        return True
    else:
        return False

#nums = [random.randint(1, 9) for _ in range(6)]
nums = [1, 2, 6, 2, 6, 2, 1]
answer = []

for i_num in range(len(nums)):
    if polindrom(nums[i_num : len(nums)]):
        answer = nums[: i_num]
        answer.reverse()
        break

print(f'Исходный список {nums}')
print(f'Нужное кол-во чисел {len(answer)}')
print(f'Список этих чисел {answer}')