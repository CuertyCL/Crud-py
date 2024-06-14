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
        cur.execute("SELECT id, user, passwd FROM usuarios WHERE user = ?", (usuario,))
        res = cur.fetchone()

        # Finalizar Conexion
        cur.close()
        conn.close()

        is_admin = False
        user = False
        passwd = False

        # Verificar si tanto usuario como contraseña son correctos
        if res is None:
            return user, passwd, is_admin
        elif res[2] == passwd_hash:
            if res[0]==1:
                is_admin = True
            user = True
            passwd = True
            return user, passwd, is_admin 
        else:
            user = True
            return user, passwd, id_user

