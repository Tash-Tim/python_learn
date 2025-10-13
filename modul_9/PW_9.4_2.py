import os
def file_list(direct, targer):
    path_list = []
    for i_elem in os.listdir(direct):
        path = os.path.join(direct, i_elem)
        if i_elem in targer:
            path_list.append(path)
        elif os.path.isdir(path):
            result = file_list(path, targer)
            if result:
                path_list.extend(result)
    return path_list


local_dir = os.path.abspath('..')
proj_name = ('PW_9.1_1.py', 'PW_9.1_2.py', 'PW_9.1_3.py', 'PW_9.2_1.py', 'PW_9.2_2.py', 'PW_9.3_1.py', 'PW_9.3_2.py')
projects_dirs = file_list(local_dir, proj_name)


for i_project in projects_dirs:
    open_project = open(i_project, 'r', encoding='utf-8')
    for i_line in open_project:
        project_text = ''
        project_text += i_line
        copy_text = open('Copy_file.txt', 'a', encoding='utf-8')
        copy_text.write(project_text)
    copy_text.write('\n' + '*' * 40 +'\n')
open_project.close()
copy_text.close()


