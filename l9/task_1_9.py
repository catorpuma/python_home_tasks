# task_1_9
"""
Создать класс TrafficLight (светофор):
●определить у него один атрибут color (цвет) и метод running (запуск);
●атрибут реализовать как приватный;
●в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
●
продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
●
переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
●
проверить работу примера, создав экземпляр и вызвав описанный метод.
"""


class TrafficLight:
    def __init__(self):
        self.__color = 'Красный'

    def running(self):
        import time

        print(self.__color)
        time.sleep(7)

        self.__color = 'Желтый'
        print(self.__color)
        time.sleep(2)

        self.__color = 'Зеленый'
        print(self.__color)
        time.sleep(2)


tl1 = TrafficLight()
tl1.running()