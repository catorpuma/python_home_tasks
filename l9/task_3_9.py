# task_3_9
"""
3. Реализовать базовый класс Worker (работник):
●определить атрибуты: name, surname, position (должность), income (доход);
●последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};

●создать класс Position (должность) на базе класса Worker;
●в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
●
проверить работу примера на реальных данных: создать экземпляры класса
 Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}

    def get_income(self):
        return self.__income


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        t_i_w = self.get_income()['wage']
        t_i_b = self.get_income()['bonus']
        return t_i_w + t_i_b


w1 = Position('Иван', 'Петров', 'Слесарь', 100, 15)
print(w1.get_full_name())
print('Доход:', w1.get_total_income())
