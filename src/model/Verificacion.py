import hashlib
import sqlite3

class Verificacion:
    def __init__(self):
        pass

    @staticmethod
    def verificar(usuario, contraseña):
        # Iniciar Conexion
        conn = sqlite3.connect("./db/usuarios.db")
        cur = conn.cursor()

        h = hashlib.new("SHA256")
        h.update(contraseña.encode())

        passwd_hash = h.hexdigest()

        # Ejecuta la consulta para buscar al usuario
        cur.execute("SELECT user, passwd FROM usuarios WHERE user = ?", (usuario,))
        res = cur.fetchone()

        # Finalizar Conexion
        cur.close()
        conn.close()

        # Verificar si tanto usuario como contraseña son correctos
        if res is None:
            return False, False 
        elif res[1] == passwd_hash:
            return True, True  
        else:
            return True, False  

