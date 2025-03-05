dbtr_name = input('Имя должника: ')
dbtr_amnt = int(input('Сумма долга: '))

messeg = ('{0}, {0}, привет. Как дела? Ты мне должен {1}$. Когда венёшь мои {1}? Аа {0}...'.
          format(dbtr_name, dbtr_amnt)
          )

print(messeg)