# task_3_11
"""
3. Создать собственный класс-исключение, который должен проверять содержимое
 списка на
наличие только чисел. Проверить работу исключения на реальном примере.
 Запрашивать у
пользователя данные и заполнять список необходимо только числами.
 Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
 пока
пользователь сам не остановит работу скрипта, введя, например, команду «stop».
 При этом
скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для этого задания примем, что пользователь может вводить только
 числа и
строки.

 Во время ввода пользователем очередного элемента необходимо реализовать
проверку типа элемента.

Вносить его в список, только если введено число.

 Класс-исключение
должен не позволить пользователю ввести текст (не число) и отобразить
 соответствующее
сообщение.

При этом работа скрипта не должна завершаться.
"""
value_list = []


class ListExeption(Exception):
    pass


while True:
    try:
        user_value = input('Введите число или команду "stop": ')
        if not user_value.isdigit():  # type check
            if user_value != 'stop':  # if not a digit check for 'stop'
                raise ListExeption()
            else:
                break  # exit
        else:
            value_list.append(user_value)
            print('Число добавлено в список')
            continue
    except ListExeption:
        print('"Ошибка: Введеное значение не является числом, \
        или командой "stop"')
        continue

print(value_list)