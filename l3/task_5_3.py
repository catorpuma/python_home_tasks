# task5_3 j_generator
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num, flag=True):
    """ Function returns combination of random items
    collected from source lists. It takes 2 arguments:
     'num' (int number of combinations taken randomly) and
     'flag' (bool, 'True' by default, that specify the mode of
     fetching of list items. 'True' - means that 'num' takes
     any amount of combinations, but items are not unique.
     'False' - means that items(words) from the lists above
     may be taken and used only once for one combination. ) """
    joke_list = []

    if flag:
        c = 0
        while c < num:
            joke_list.append(random.choice(nouns) + ' '
                             + random.choice(adverbs) + ' '
                             + random.choice(adjectives))
            c += 1
    else:
        if num > len(nouns):
            print('too many jokes requested')
        else:
            c = 0
            while c < num:
                joke_list.append(nouns.pop(random.randrange(len(nouns))) + ' '
                                 + adverbs.pop(random.randrange(len(adverbs)))
                                 + ' '
                                 + adjectives.pop(random.randrange(len(adjectives))))
                c += 1

    return joke_list


print(get_jokes(num=10, flag=True))
