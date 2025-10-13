import os

def find_dir(project, find):
    print('Ищу в:', os.path.join(project))
    for i_dir in os.listdir(project):
        path = os.path.join(project, i_dir)
        if i_dir == find:
            print('Путь найден', path)
        elif os.path.isdir(path):
            result = find_dir(path, find)
            if result:
                break
    else:
        result = None
    return result

user_dir = os.path.abspath(os.path.join('..', '..', 'Test_dir'))
need_file = 'Test_file_.txt'


print(find_dir(user_dir, need_file))