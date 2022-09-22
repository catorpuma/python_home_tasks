# task_4_9
"""
4. Реализуйте базовый класс Car:
●
у класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
●опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
●
для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
к атрибутам,
выведите результат. Вызовите методы и покажите результат.

"""


class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = False
        print('\n')
        print('Автомобиль:', name, color)

    def show_speed(self):
        return self.speed

    def go(self, speed):
        self.speed = speed
        print(f'Едем. Скорость: {self.show_speed()}')

    def stop(self):
        self.speed = 0
        print(f'Остановка. Скорость: {self.speed}')

    def turn(self, direction):
        print(f'Поворачиваем {direction}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f' Скорость превышена. Ваша скорость {self.speed}'
        else:
            return self.speed


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f' Скорость превышена. Ваша скорость {self.speed}'
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True
        print('Is police?:', self.is_police)


class SportCar(Car):
    pass


c1 = TownCar('KIA', 'green')
c1.go(61)
c1.turn('налево')
c1.turn('прямо')
c1.stop()

p1 = PoliceCar('Ford', 'yellow')
p1.go(101)
p1.turn('налево')
p1.turn('прямо')
p1.stop()

s1 = SportCar('Ford Mustang', 'red')
s1.go(261)
s1.turn('налево')
s1.turn('прямо')
s1.stop()
