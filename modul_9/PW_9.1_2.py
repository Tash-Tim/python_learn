import os
def dirs_files(project):
    print('\nСодержимое директории: {}'.format(project))
    for i_dir in os.listdir(project):
        dirs_path = os.path.join(project, i_dir)
        print('   ', dirs_path)


proj_dir_name = ['Skillbox_basic_2', 'Python_Basic']
for i_proj in proj_dir_name:
    path_to_proj = os.path.abspath(os.path.join('..', '..', i_proj))
    dirs_files(path_to_proj)