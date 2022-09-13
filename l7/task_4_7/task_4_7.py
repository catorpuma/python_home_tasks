# task_4_7
import os


def tree_reader(path):
    f_list = []
    for r_folder, dirs, files in os.walk(path):
        for file in files:
            f_list.append(os.path.join(r_folder, file))

    return f_list


# counters
a = 0
b = 0
c = 0
d = 0

dict_u = {100: a, 1000: b, 10000: c, 100000: d}
for name in tree_reader('foo'):
    statinfo = os.stat(name)
    if statinfo.st_size < 100:
        a += 1
        dict_u[100] = a
    elif 100 < statinfo.st_size < 1000:
        b += 1
        dict_u[1000] = b
    elif 1000 < statinfo.st_size < 10000:
        c += 1
        dict_u[10000] = c
    elif 10000 < statinfo.st_size < 100000:
        d += 1
        dict_u[100000] = d
print(dict_u)
