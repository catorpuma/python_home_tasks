# task_6_6
import sys

# make list of arguments
list_l = (len(sys.argv))
arg_l = list(sys.argv[1:list_l])

if len(arg_l) < 3:
    if len(arg_l) == 0:
        with open("bakery.csv", "r") as a_file:
            print(a_file.read())

    elif len(arg_l) == 1:
        with open("bakery.csv", "r") as a_file:
            f_list = a_file.readlines()  # list of lines
            if arg_l[0].isdigit():
                x = int(arg_l[0])  # read first argument
            else:
                exit('not valid args')
            if f_list:  # if list is not empty
                for i in (f_list[(x-1):]):  # read it from x-position
                    print(i.rstrip('\n'))

    elif len(arg_l) == 2:
        with open("bakery.csv", "r") as a_file:
            f_list = a_file.readlines()  # list of lines
            if arg_l[0].isdigit():
                x = int(arg_l[0])  # read first argument
                
            else:
                exit('not valid args')
            if arg_l[1].isdigit():
                y = int(arg_l[1])  # second argument
                
            else:
                exit('not valid args')

            if f_list:  # if list is not empty
                for i in (f_list[(x-1):y]):  # read it from x-y position
                    print(i.rstrip('\n'))
