# task_1_6
import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
    for line in file:
        re_list = re.split(r'\s', line)
        t_split = (re_list[0], re_list[5][1:], re_list[6])
        print(t_split)
