# task_4_2
names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
         'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in names:
    w_list = i.split()
    l_word = w_list[-1]
    new_word = l_word.lower()
    print('Привет, ', new_word.capitalize(), '!')
