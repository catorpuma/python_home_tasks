# task_4_5_6
"""
4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий
склад. А также
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе
определить
параметры, общие для приведённых типов. В классах-наследниках реализовать
параметры,
уникальные для каждого типа оргтехники.
"""
"""
5. Продолжить работу над предыдущим заданием. Разработать методы, которые
 отвечают за
приём оргтехники на склад и передачу в определённое подразделение компании. Для
хранения данных о наименовании и количестве единиц оргтехники, а также других
 данных,
можно использовать любую подходящую структуру (например, словарь).
"""
"""
6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации
вводимых
пользователем данных. Например, для указания количества принтеров,
отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум
возможностей,
изученных на уроках по ООП.
"""

# Office equipment items


class OfficeEquip():  # base class
    def __init__(self, type, name):
        self.type = type
        self.name = name


class Scanner(OfficeEquip):
    def __init__(self, type, name, lamp):
        self.type = type
        self.name = name
        self.paper = lamp


class Printer(OfficeEquip):
    def __init__(self, type, name, toner):
        self.type = type
        self.name = name
        self.toner = toner


class Store():
    def __init__(self) -> None:
        self.store_dict = []

    def accept_new_equipment(self):

        def input_type():
            office_equipment_type = None
            while True:

                try:
                    office_equipment_type = int(
                        input('Введите тип принимаемой оргтехники \
                         1 -Принтер, 0 - Сканнер:'))
                except Exception:
                    print("Введите числовые данные")
                if office_equipment_type == 1 or office_equipment_type == 0:
                    break
                else:
                    print('введите число 1 или 0')
                    continue
            return office_equipment_type

        def input_params():
            office_equipment_name = None
            office_equipment_param = None
            equipment_type = None
            while True:
                if input_type() == 1:
                    equipment_type = 'Принтер'
                    office_equipment_name = input('Введите имя принтера:')
                    try:
                        office_equipment_param = int(
                            input('Введите количество тонера:'))
                    except Exception:
                        print("Введите числовые данные")
                        continue
                    break
                else:
                    equipment_type = 'Сканнер'
                    office_equipment_name = input('Введите имя сканнера:')
                    try:
                        office_equipment_param = int(
                            input('Введите ресурс лампы:'))
                    except Exception:
                        print("Введите числовые данные")
                        continue
                    break
            if equipment_type == 'Сканнер':
                return Scanner(equipment_type, office_equipment_name, office_equipment_param)
            else:
                return Printer(equipment_type, office_equipment_name, office_equipment_param)
        self.store_dict.append(input_params())

    def show_store(self):
        if self.store_dict:
            for i in self.store_dict:
                print(f'Состав склада:{i.type} {i.name}')


# methods of Store class
new_store = Store()
new_store.accept_new_equipment()
new_store.accept_new_equipment()
new_store.show_store()
