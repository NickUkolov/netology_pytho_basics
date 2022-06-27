import os
from pprint import pprint


def file_path(file_name):
    for root, directory, files in os.walk('.'):
        for file in files:
            if file == file_name:
                return os.path.join(root, file)


def cook_book(file_name):
    dish_book = {}
    with open(file_path(file_name), encoding='utf-8') as dishes:
        for row in dishes:
            dish_name = row.strip()
            dish_book[dish_name] = []
            ingr_quantity = int(dishes.readline())
            for _ in range(ingr_quantity):
                ingr, quantity, measure = dishes.readline().strip().split(' | ')
                ingr_list = {'ingr_name': ingr, 'quantity': int(quantity), 'measure': measure}
                dish_book[dish_name].append(ingr_list)
            dishes.readline()
    return dish_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            ingr_name = ingr.get('ingr_name')
            if ingr_name in shop_list:
                shop_list[ingr_name]['quantity'] += ingr['quantity'] * person_count
            else:
                ingr['quantity'] *= person_count
                shop_list[ingr_name] = ingr
    return shop_list


def write_result_file(*file_names):
    file_dictionary = {}
    for file_name in file_names:
        with open(file_path(file_name), encoding='utf-8') as file_read:
            file_dictionary[file_name] = file_read.readlines()
    with open('result.txt', 'w', encoding='utf-8') as file_write:
        for file in sorted(file_dictionary, key=file_dictionary.get, reverse=True):
            file_write.write(f'{file}\n{len(file_dictionary[file])}\n{"".join(file_dictionary[file])}\n\n')


cook_book = cook_book('recipes.txt')
pprint(cook_book, sort_dicts=False, width=100)

pprint(get_shop_list_by_dishes(['Фахитос', 'Утка по-пекински'], 2), sort_dicts=False, width=100)

write_result_file('1.txt', '2.txt', '3.txt')