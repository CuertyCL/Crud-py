import hashlib
import sqlite3

class Verificacion:
    def __init__(self):
        pass

    def verificar(usuario, contraseña):
        # Iniciar Conexion
        conn = sqlite3.connect("usuarios.db")
        cur = conn.cursor()

        h = hashlib.new("SHA256")
        h.update(contraseña.encode())

        passwd_hash = h.hexdigest()

        cur.execute("SELECT user, passwd FROM usuarios WHERE user = ? AND passwd = ?", (usuario, passwd_hash))

        resultado = cur.fetchone()

        # Finalizar Conexion
        cur.close()
        conn.close()

        # Verificar si se encontró un resultado
        if resultado is not None:
            return True
        return False
    

