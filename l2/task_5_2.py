# task_5_2
items = [19.44, 11.10, 57.1, 45, 432, 11.32, 44.5, 88.0, 98.17, 100]
print('список до сортировки:')
print(items)
print('идентификатор объекта списка (до сортировки):', id(items))
print()  # split

items.sort()  # list sorting
r_items = sorted(items, reverse=True)  # list reversed sorting
print('список после сортировки по возрастанию:')
print(items)
print('идентификатор объекта списка (п./с. по возрастанию):', id(items))

for i in items: 
    # formating of prices for output:
    if str(i).find('.') == -1:
        items[items.index(i)] = str(items[items.index(i)]) + ' руб 00 коп'
    if str(i)[::-1].find('.') == 1:
        dot_f = str(items[items.index(i)])[:].find('.')
        items[items.index(i)] = str(items[items.index(i)])[
            :dot_f] + ' руб ' + '0' \
                    + str(items[items.index(i)])[dot_f+1:] + ' коп'
    if str(i)[::-1].find('.') > 1:
        dot_f = str(items[items.index(i)])[:].find('.')
        items[items.index(i)] = str(items[items.index(i)])[
            :dot_f] + ' руб ' + str(items[items.index(i)])[dot_f+1:] + ' коп'

s = [str(b) for b in items]
print('='*8)  # visual spliter
print('форматированный вывод цен товаров (по возрастанию):')
print(', '.join(s))

ex_list = items[-5:len(items)]  # fetching of most expensive goods
ex_s = [str(b) for b in ex_list]
print('список пяти самых дорогих товаров (по возрастанию):')
print(', '.join(ex_s))
print('='*8)  # visual spliter

for i in r_items:
    if str(i).find('.') == -1:
        r_items[r_items.index(i)] = str(
            r_items[r_items.index(i)]) + ' руб 00 коп'
    if str(i)[::-1].find('.') == 1:
        dot_f = str(r_items[r_items.index(i)])[:].find('.')
        r_items[r_items.index(i)] = str(r_items[r_items.index(i)])[
            :dot_f] + ' руб ' + '0' \
                    + str(r_items[r_items.index(i)])[dot_f+1:] + ' коп'
    if str(i)[::-1].find('.') > 1:
        dot_f = str(r_items[r_items.index(i)])[:].find('.')
        r_items[r_items.index(i)] = str(r_items[r_items.index(i)])[
            :dot_f] + ' руб ' + str(r_items[r_items.index(i)])[
                dot_f+1:] + ' коп'

s = [str(b) for b in r_items]
print('форматированный вывод цен товаров (по убыванию):')
print(', '.join(s))
