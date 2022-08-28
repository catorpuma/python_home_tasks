# task_4_4
import requests


def currency_rates(c_arg):
    """ The function returns float value for currency charcode
    corresponding the ruble (skipping the currency nominal 'as is')"""

    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    page_in = r.text  # fetching text of request

    # form list of currency charcodes (to exclude input errors):
    list_of_codes = []  # valute charcodes collection
    code_inx = -1  # tags index counter (thnks to stackoverflow)
    code_tag = '<CharCode>'
    code_close_tag = '</CharCode>'
    while True:
        # fetching of charcode tags index with start position offset
        code_inx = page_in.find(code_tag, code_inx + 1)
        c_code_inx = page_in.find(code_close_tag, code_inx + 1)
        if code_inx == -1:
            break

        # fill out the list of valute codes
        # (leave '>' to "walkaround" discarding of chars
        #  by lstrip() method - look for 'f'-string below)
        list_of_codes.append(page_in[code_inx:c_code_inx].lstrip('<CharCode'))

    # check the currency exists in the collection of codes (t/w reg.casting):
    flag = (list_of_codes.count(f'>{str(c_arg).upper()}'))
    if flag == 0:
        return None  # returns None if user charcode doesn't suit

    # extract value of currency rate (skipping the nominal) using
    # 'str'-class methods :
    u_split = page_in.split(c_arg, 1)[1]
    res = (u_split[u_split.find('<Value>')
           :u_split.find('</Value>')].lstrip('<Value>'))
    f_res = float(res.replace(',', '.'))
    c_date = page_in[page_in.find('Date=')+5:(page_in.find('Date='))+17]
    return f'{round(f_res,2)} {c_date} '
