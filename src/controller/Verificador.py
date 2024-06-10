from model.Verificacion import Verificacion


class Verificador:

    valid = False
    open = True

    def __init__(self):
        pass

    def iniciarsesion(self, root, entry_user, entry_passwd):
        user = entry_user.get()
        passwd = entry_passwd.get()
        v = Verificacion.verificar(usuario=user, contraseña=passwd)
        if v:
            root.destroy()
            self.valid = True
            self.open = False
        self.valid = False
        self.open = True

    def get_valid(self):
        return self.valid

    def cerrar_ventana(self, root):
        root.destroy()

            
VER = Verificador()