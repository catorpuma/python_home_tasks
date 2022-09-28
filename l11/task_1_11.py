# task_1_11
"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый — с
декоратором @classmethod. Он должен извлекать число, месяц, год и
 преобразовывать их тип
к типу «Число». Второй — с декоратором @staticmethod, должен проводить
 валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
 структуры на
реальных данных.
"""


class Number(object):  # new type "Число"
    def __init__(self, string):
        self.string = string
        self.cnv()

    def cnv(self):
        self.num = int(self.string)

    def __str__(self):
        return '{0}'.format(self.num)

    def __lt__(self, other):
        return self.num < other

    def __gt__(self, other):
        return self.num > other


class Date():  # class "Дата"
    dd, mm, yyyy = '', '', ''

    def __init__(self, d_string):
        self.arg = d_string
        Date.helper(self.arg)
        Date.validator_c(self.arg)
        pass

    def pattern_check(arg):  # check for pattern "день-месяц-год"
        import re
        date_pattern = "^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}$"
        if re.match(date_pattern, arg) is None:
            return False
        else:
            return True

    @classmethod
    def helper(cls, arg):
        cls.arg = arg
        if Date.pattern_check(cls.arg):
            d = arg[0:2]
            m = arg[3:5]
            y = arg[6:]
            # casting to "Число" type:
            cls.dd = Number(d)
            cls.mm = Number(m)
            cls.yyyy = Number(y)
            print('дата:', cls.dd, '-', cls.mm, '-', cls.yyyy,
                  'приведена к типу', type(cls.dd))  # debug

    @staticmethod
    def validator_c(arg):  # value validation
        if not Date.pattern_check(arg):
            print('Дата не соотв. формату "дд-мм-гггг"')
        else:
            if Date.dd > 0 and Date.dd < 32:
                print('Число дней верное')
            else:
                print('Число дней не верное')

            if Date.mm > 0 and Date.mm < 13:
                print('Число месяцев верное')
            else:
                print('Число месяцев не верное')
            print('\n')


# check-run
Date('10-21-2022')
Date('32-12-2022')
Date('1-1-1')
