
import tkinter as tk
import sqlite3 as sql
from tkintertable import TableCanvas, TableModel
import csv
import os

def get_data(database, table):
    conn = sql.connect(database=database)
    cursor = conn.cursor()

    res = cursor.execute(f'SELECT * FROM {table}').fetchall()

    cursor.close()
    conn.close()
    return res

def show_data(list):
    for i in range(len(list)-1):
        for j in range(len(list[i])-1):
            print(list[i][j], end=", ")
        print()

def get_table_info(database, table):
    conn = sql.connect(database=database)
    cursor = conn.cursor()

    # Saca Información de la tabla, como nombre, tipo de dato, etc
    res = cursor.execute(f"PRAGMA table_info({table});").fetchall()

    cursor.close()
    conn.close()
    return res

def get_index_data(list, index):
    # Retorna solamente la columna indicada de una tabla dada

    new_list = []
    for i in range(len(list)):
        new_list.append(list[i][index])
    return new_list

def ventana(csv):
    root = tk.Tk()

    data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
        'rec2': {'col1': 99.88, 'col2': 108.79, 'label': 'rec2'}
        }

    frame = tk.Frame(root)

    tabla = TableCanvas(frame, read_only=True)
    tabla.importCSV(csv, sep=";")
    tabla.show()

    frame.pack()

    root.mainloop()


def import_to_csv(csv_name, list, columns):
    if not os.path.isfile(csv_name):
        open(csv_name, "x")
    with open(csv_name, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=";",
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columns)
        for i in range(len(list)):
            writer.writerows(list)


# import_to_csv("eggs.csv", get_data("inventario.db", "inventario"))

import_to_csv(csv_name="eggs.csv", 
              list=get_data("inventario.db", "inventario"), 
              columns=get_index_data(get_table_info("inventario.db", "inventario"), 1)
              )

ventana("eggs.csv")





# list = get_index_data(get_table_info("inventario.db", "inventario"), 1)
# print(list)
# print(show_data(get_data("inventario.db", "inventario")))

# lista = []

# set1 = {
#      'name': 'Michael',
#      'place': 'USA',
#      }

# set2 = {
#      'name': 'Trevor',
#      'place': 'USA',
#      }

# set3 = {
#      'name': 'Franklin',
#      'place': 'USA',
#      }

# lista.append(set1)
# lista.append(set2)
# lista.append(set3)

# print(lista)

# def convert(lst):
#    res_dict = {}
#    for i in range(0, len(lst), 2):
#        res_dict[lst[i]] = lst[i + 1]
#    return res_dict
 
# lst = ['a', 1, 'b', 2, 'c', 3]
# print(convert(lst))
