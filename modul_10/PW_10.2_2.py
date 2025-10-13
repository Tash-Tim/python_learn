ages_file = None
result_file = None

try:
    ages_file = open('ages.txt', 'r', encoding='utf-8')
    result_file = open('result.txt', 'w', encoding='utf-8')
except (FileExistsError, PermissionError, IsADirectoryError, FileNotFoundError) as err:
    print("Поймано исключение: ", err, type(err))

try:
    if ages_file and result_file:
        names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        ind_num = 0
        for i_ages in ages_file:
            try:
                clear_ages = i_ages.strip()
                int(clear_ages)
                result_file.write(names[ind_num] + ' - ' + clear_ages + '\n')
                ind_num += 1
            except (TypeError, ValueError) as exc:
                print("Поймано исключение: ", exc, type(exc))
        ages_file.close()
        result_file.close()
except NameError as all_err:
    print("Поймано исключение: ", all_err, type(all_err))