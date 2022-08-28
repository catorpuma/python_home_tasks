# task_3_3 thesaurus() - supposed that all names are started with uppercase
def thesaurus(*args):
    args_l = list(args)  # list for names
    args_l.sort()
    letters = []  # list for letters
    dict_args = {}  # dict for return

    for item in args_l:
        letters.append(item[0])  # get the first letter for every argument
    letter_set = set(letters)  # get the unique keys

    for letter in letter_set:
        l_values = []  # list of names for every letter
        for name in args_l:
            if name[0] == letter:
                l_values.append(name)  # build list of corresponding names
        dict_args[letter] = l_values  # insert key-value into dictionary
    return dict_args


m = thesaurus('Иван', 'Мария', 'Петр', 'Илья')
print(m)
