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