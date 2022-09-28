# task_7_11
"""
7. Реализовать проект «Операции с комплексными числами». Создать
 класс «Комплексное
число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса
 (комплексные числа),
выполнить
сложение
и умножение созданных экземпляров. Проверить корректность
 полученного результата.
"""


class ComplexNumber(object):
    def __init__(self, real_part, i_part=0):
        self.real_part = real_part
        self.i_part = i_part
        self.cnv_r()
        self.cnv_i()

    def cnv_r(self):
        self.real_part = float(self.real_part)

    def cnv_i(self):
        self.i_part = float(self.i_part)

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part,
                             self.i_part + other.i_part)

    def __str__(self):
        return '(%g, %g)' % (self.real_part, self.i_part)

    def __mul__(self, other):
        return ComplexNumber(self.real_part*other.real_part - self.i_part*other.i_part,
                             self.i_part*other.real_part + self.real_part*other.i_part)


c1 = ComplexNumber(2, 4)
c2 = ComplexNumber(5, 6)
print(c1 + c2)
print(type(c1 + c2))
