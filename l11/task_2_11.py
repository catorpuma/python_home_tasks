# task_2_11
"""
2. Создать собственный класс-исключение, обрабатывающий ситуацию деления
на ноль.
Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться
с ошибкой.
"""


class userdivision(Exception):
    pass


while True:
    try:
        user_num_0 = int(input("Введите делимое: "))
        user_num_1 = int(input("Введите делитель: "))
        if user_num_1 == 0:
            raise userdivision
        else:
            res = user_num_0/user_num_1
            print('результат деления: ', res)
            break
    except userdivision:
        print('На ноль делить нельзя')
        print('\n')
        continue

print('выход')
