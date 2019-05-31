import glob
import csv
import re


def get_data():
    temp_dict={}
    os_prod_list=[]
    os_name_list=[]
    os_code_list=[]
    os_type_list=[]
    main_data = [['Изготовитель системы', 'Название ОС','Код продукта','Тип системы']]
    for filename in glob.glob('Lesson2_data/*.txt'):
        with open(filename) as file:
            for line in file:
                line=re.sub("\s+", " ", line)
                key, *value = line.split(':', maxsplit=1)
                temp_dict[key] = value

            os_prod_list.append(str(temp_dict[main_data[0][0]])[2:-2])
            os_name_list.append(str(temp_dict[main_data[0][1]])[2:-2])
            os_code_list.append(str(temp_dict[main_data[0][2]])[2:-2])
            os_type_list.append(str(temp_dict[main_data[0][3]])[2:-2])
        temp_dict.clear()
    temp_list =[os_prod_list,os_name_list,os_code_list,os_type_list]
    n=len(main_data[0])

    for i in range(n):
        main_data.append(temp_list[i])

    with open ('Lesson2_data/main_data.doc','w', encoding='utf-8') as f:
        for item in main_data:
            f.write("%s\n" % item)
    return main_data



def write_to_csv():
    with open("Lesson2_data/список.csv", "w", newline='') as file_new:
        new_list = get_data()
        csv.writer(file_new).writerow(new_list[0])
        new_list = zip(*new_list[1:])
        for item in new_list:
            csv.writer(file_new).writerow(item)
    with open('Lesson2_data/список.csv') as f_n:
        f_n_reader = csv.reader(f_n)
        for row in f_n_reader:
            print(row)


write_to_csv()



