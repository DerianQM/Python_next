import yaml

load_dict ={'34у': [1,2,3], '23м':23, '12ы': {'e':'str','f':17},}
print(load_dict)


with open('Lesson2_data/data_write.yaml', 'w', encoding='UTF-8') as f_n:
    yaml.dump(load_dict, f_n, default_flow_style=True, allow_unicode=True)

with open('Lesson2_data/data_write.yaml', encoding='UTF-8') as f_n:
    print(f_n.read())