# task_3_6
users_lst = []
hobby_lst = []

with open('users.csv', 'r', encoding='utf-8') as u_file:
    for line in u_file:
        users_lst.append(line.rstrip())

with open('hobby.csv', 'r', encoding='utf-8') as h_file:
    for line in h_file:
        hobby_lst.append(line.rstrip())

import itertools

if len(hobby_lst)>len(users_lst):
    exit('1')
else:
    rez = itertools.zip_longest(users_lst, hobby_lst, fillvalue=None)
    file = open('dict.txt', 'w')
    print(dict(rez), file=file)
    file.close()


