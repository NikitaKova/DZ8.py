




from init import init
from controller import *


init()
greeting()
start()

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

