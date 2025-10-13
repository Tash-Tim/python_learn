word_list = []

while True:
    try:
        word= input('Enter word: ')
        if word.lower() == 'error':
            raise BaseException("You're broke program")
        if not word.isalpha():
            raise TypeError
        word_list.append(word)
        if len(word_list) == 5:
            print('No place')
            break
    except TypeError:
        print("You're entered digit" )
    except BaseException:
        word_list = []
        print('Stop word entered')
        raise ValueError("Don't enter stop word")

    finally:
        print('List len:', word_list)

write_to = open('Add_10.4.txt', 'w')
write_to.write('\n'.join(word_list))
write_to.close()