# task_1_3 zero one two three four five six seven eight nine ten
NUM_DICT = {'zero': '"ноль"', 'one': '"один"', 'two': '"два"',
            'three': '"три"', 'four': '"четыре"', 'five ': '"пять"',
            'six': '"шесть"', 'seven': '"семь"', 'eight': '"восемь"',
            'nine': '"девять"', 'ten': '"десять"'}


def num_translate(word):
    tr = ''
    for key, value in NUM_DICT.items():
        if word == key:
            tr = value
            break
        else:
            tr = None
    return tr


print(num_translate("ten"))
