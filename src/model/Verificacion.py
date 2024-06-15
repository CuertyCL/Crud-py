import hashlib
import sqlite3

class Verificacion:
    def __init__(self):
        self.is_admin = False

    def verificar(self, usuario, contraseña):
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

        user = False
        passwd = False

        # Verificar si tanto usuario como contraseña son correctos
        if res is None:
            return user, passwd, self.is_admin
        elif res[2] == passwd_hash:
            # Verificar si el usuario es admin
            if res[0]==1:
                self.is_admin = True
            user = True
            passwd = True
            self.nombre = res[1]
            self.contraseña = res[2]
            return user, passwd, self.is_admin 
        else:
            user = True
            return user, passwd, self.is_admin
        
    def get_nombre(self):
        return self.nombre
    
    def get_passwd(self):
        return self.contraseña
    
    def get_is_admin(self):
        return self.is_admin

