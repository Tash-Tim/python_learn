
def add_num(num, lst=None): # ПРАВИЛЬНО
    lst = lst or []
    if not lst:
        lst = []
    lst.append(num)
    print(lst)


add_num(5, [1, 2, 3])
add_num(10)
add_num(20)