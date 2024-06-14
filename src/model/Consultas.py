import sqlite3

class Consultas:
    def __init__(self, database):
        self.database = database

    def get_data(self, table, column='*'):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT {column}
                        FROM {table};""")
        
        res = cursor.fetchall()

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

    def get_title(self, table, index=1):
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

