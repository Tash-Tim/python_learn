def polin_check(get_word):
    if get_word == get_word[::-1]:
        return True
    else:
        return False

words_file = open('words.txt', 'r', encoding='utf-8')
error_logs = open('errors.txt', 'a', encoding='utf-8')
polin_cnt = 0
words_num = 0

try:
    for i_word in words_file:
        words_num +=1
        try:
            clear_i_word = i_word.lower().strip()
            if clear_i_word.isalpha():
                polin_cnt += polin_check(clear_i_word)
            else:
                raise ValueError(f'Wors N{words_num} contains digit')
        except (ValueError, TypeError, FileNotFoundError, FileExistsError) as err:
            print('Except detected', err, type(err))
            error_logs.write(str(err) + '\n')


finally:
    print('Number of polynder wors', polin_cnt)
    words_file.close()
    error_logs.close()




