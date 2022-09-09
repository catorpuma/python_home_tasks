# task_6_6
import sys

# make list of arguments
list_l = (len(sys.argv))
arg_l = list(sys.argv[1:list_l])
if len(arg_l) <= 1:
    if len(arg_l) == 0:
        pass
    elif len(arg_l) == 1:
        i = arg_l[0]
        with open("bakery.csv", "a") as a_file:
            
            a_file.write(f'{i}')
            a_file.write("\n")

if len(arg_l) > 1:
    print('Please enter valid number of arguments')
