




from init import init
from controller import *


init()
greeting()
start()

from input_data import input_data
from write_data import write_data


def push_data():
    dct = input_data()

    # id;surname;name;class;status   - name.csv
    write_data([dct.get("id"), dct.get("surname"), dct.get("name"), dct.get("class"), dct.get("status")], "name.csv")

    # id;city;street;house;apartament;other  - class.csv
    write_data([dct["id"], dct["city"], dct["street"], dct["house"], dct["apartament"], dct["other"]], "adress.csv")

    # id;row;col - adress.csv
    write_data([dct["id"], dct["row"], dct["col"]], "class.csv")


def read_data():
    lst_name = []
    with open('name.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_name.append(temp)
        print(lst_name)
    lst_adress = []
    with open('adress.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_adress.append(temp)
        print(lst_adress)

    lst_class = []
    with open('class.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_class.append(temp)
        print(lst_class)

    lst = []
    for i in range(len(lst_name)):
        lst.append([lst_name[i][0], lst_name[i][1], lst_name[i][2], lst_name[i][3], lst_name[i][4], \
            lst_class[i][1], lst_class[i][2], \
            lst_adress[i][1], lst_adress[i][2], lst_adress[i][3], lst_adress[i][4], lst_adress[i][5]])
    return lst



def print_data(data, search = False):
    if len(data) > 0:
        print("id".center(5), "Фамилия".center(20), "Имя".center(10), "Класс".center(6), "Статус".center(6),\
           "Ряд".center(4), "Парта".center(6),\
            "Город".center(15), "Улица".center(15), "Дом".center(6), "Квартира".center(4), "Примечание".center(20))
        print("-"*120)
        if not search:
            del data[0]
        for item in data:
            print(item[0].center(5), item[1].center(20), item[2].center(10), item[3].center(6), item[4].center(6),\
           item[5].center(4), item[6].center(6),\
            item[7].center(15), item[8].center(15), item[9].center(6), item[10].center(4), item[11].center(20))
    else:
        print("\n")
        print("*"*100 + "\nСправочник пуст!\n" + "*"*100)
        print("\n")

from read_data import read_data
from print_data import print_data

def search_data(word, data):
    if len(data) > 0:
        lst = []
        for item in data:
            if word in item:
                lst.append(item)
        if lst == []:
            return None
        else:
            return lst
    else:
        return None

from push_data import *
from read_data import *
from print_data import *
from search_data import *


def greeting():
    print("Здравствуйте!")

def start():
    print("Что желаем сделать:\n\
    1 - получить всю информацию о учениках;\n\
    2 - добавить ученика;\n\
    3 - поиск ученика;\n\
    4 - выход.")
    ch = input("Введите цифру: ")
    while True:
        if ch == '1':
            data = read_data()
            print_data(data)
            start()
        elif ch == '2':
            push_data()
            start()
        elif ch == '3':
            info = input("Введите данные для поиска: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Данные не обнаружены")                
            start()
        elif ch == '4':
            print("Сеанс окончен, до свидания!")
            break
        else:
            print("Введите корректную цифру!")
            start()

from read_data import read_data


def init():
    if not (len(read_data()) > 0):
        
        with open("name.csv", 'a+') as file:
            file.write("id;surname;name;class;status\n")

        with open("adress.csv", 'a+') as file:
            file.write("id;city;street;house;apartament;other\n")

        with open("class.csv", 'a+') as file:
            file.write("id;row;col\n")

from write_data import count_data

def input_data():
    dct = dict()
    Id = count_data("name.csv") 
    dct["id"] = Id     # list[0] - это Id ученика
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["class"] = input('Введите Класс: ')
    dct["status"] = input('Введите Статус: ')
    dct["row"] = input('Введите Ряд: ')
    dct["col"] = input('Введите Номер парты: ')
    dct["city"] = input('Введите Город: ')
    dct["street"] = input('Введите Улица: ')
    dct["house"] = input('Введите Дом: ')
    dct["apartament"] = input('Введите Квартира: ')
    dct["other"] = input('Введите Примечание: ')
    return dct


def write_data(data, name):
    with open(name, 'a+') as file:
        file.write(";".join(map(str, data)))
        file.write(f"\n")


def count_data(name):
    with open(name, 'r') as file:
        data = file.read()
    return data.count('\n')
