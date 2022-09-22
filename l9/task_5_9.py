# task_5_9
"""
5. Реализовать класс Stationery (канцелярская принадлежность):
определить в нём атрибут title (название) и метод draw (отрисовка).
Метод выводит
сообщение «Запуск отрисовки»;
●создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
●в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
●
создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        draw_ = 'Запуск отрисовки'
        return draw_


class Pen(Stationery):

    def draw(self):
        draw_ = 'Чернила'
        return draw_


class Pencil(Stationery):

    def draw(self):
        draw_ = 'Грифель'
        return draw_


class Handle(Stationery):

    def draw(self):
        draw_ = 'Маркер'
        return draw_


p1 = Pen('Ручка')
print(p1.draw())

pn1 = Pencil('Карандаш')
print(pn1.draw())

h1 = Handle('Маркер')
print(h1.draw())
