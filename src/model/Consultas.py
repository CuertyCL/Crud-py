import sqlite3

class Consultas:
    def __init__(self, database):
        self.database = database

    def get_data(self, table, column='*', specify_column=False, index=0):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT {column}
                        FROM {table};""")
        
        res = cursor.fetchall()

        cursor.close()
        conn.close()

        if specify_column:
            list = []
            for i in range(len(res)):
                list.append(res[i][index])
            return list
        else:
            return res
    
    def get_specific_data(self, table, column, name) -> list[str]:
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT *
                        FROM {table}
                        WHERE {column} = ?;""", (name,))
        
        res = cursor.fetchone()

        cursor.close()
        conn.close()
        return res

    def show_data(self, data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                if j == len(data[i])-1:
                    print(data[i][j], end='')
                else:
                    print(data[i][j], end=', ')
            print()

    def get_title(self, table, index=1) -> list[str]:
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute(f"PRAGMA table_info({table});")
        
        res = cursor.fetchall()

        cursor.close()
        conn.close()

        list = []
        for i in range(len(res)):
            list.append(res[i][index])
        return list
    
    def show_title(self, titles):
        for i in range(len(titles)):
            if i == len(titles)-1:
                print(titles[i], end='')
            else:
                print(titles[i], end=', ')

    def insert_data_inventario(self, nombre=str, clase=int, lugar=int, unidad=int,precio=float, stock_min=int, stock_max=int, stock=int) -> None:
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        values = [nombre, clase, lugar, unidad, precio, stock_min, stock_max, stock]

        cursor.execute("""INSERT INTO inventario(nombre, id_clase, id_lugar, id_unidad, precio, stock_minimo, stock_maximo, stock)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", values)
        
        conn.commit()

        values = []

        cursor.close()
        conn.close()

    def get_id_from_column(self, column, table, name) -> int:
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT *
                        FROM {table}
                        WHERE {column} = '{name}';""")
        
        res = cursor.fetchone()

        cursor.close()
        conn.close()

        return int(res[0])
    
    def get_name_from_id(self, column, table, id) -> str:
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT *
                        FROM {table}
                        WHERE {column} = '{id}';""")
        
        res = cursor.fetchone()

        cursor.close()
        conn.close()

        if res[1]==None:
            res[1] = ""

        return str(res[1])
    
    def delete_record(self, column, table, where):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute(f"""DELETE FROM {table}
                       WHERE {column} = ?""", (where,))
        
        conn.commit()

        cursor.close()
        conn.close()

        
    
