# This is a python script for task3 lesson1.

i = 1
while i <= 100:
    suffix = ''
    if i % 10 == 1 and i != 11:
        suffix = 'т'
    elif i % 10 == 2 and i != 12:
        suffix = 'та'
    elif i % 10 == 3 and i != 13:
        suffix = 'та'
    elif i % 10 == 4 and i != 14:
        suffix = 'та'
    else:
        suffix = 'тов'
    print(i, ' процен'+suffix)
    i += 1
