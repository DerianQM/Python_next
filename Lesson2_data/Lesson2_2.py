'''
Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
'''



import json
import datetime
import os

list_val= ['item','quantity','price','buyer','date']

dict_to_json={}

def write_order_to_json(list_val):
    for name in list_val:
        if name == 'quantity':
            dict_to_json[name] = int(input(f'Введите - {name}'))
        elif name == 'price':
            dict_to_json[name] = float(input(f'Введите - {name}'))
        elif name == 'date':
            ds = datetime.datetime.now()
            date = ds.strftime('%Y-%m-%d_%H%M')
            dict_to_json[name] = date
        else:
            dict_to_json[name] = input(f'Введите - {name}')
    path='orders.json'
    if os.path.exists(path):
        with open(path, 'a', encoding='UTF-8') as f_n:
            json.dump(dict_to_json, f_n,  indent=4)
    else:
        with open(path, 'w', encoding='UTF-8') as f_n:
            json.dump(dict_to_json, f_n,  indent=4)
    with open(path,'r', encoding='UTF-8') as f_n:
        print(f_n.read())


write_order_to_json(list_val)