from model.Verificacion import Verificacion

def iniciarsesion(root, entry_user, entry_passwd):
        user = entry_user.get()
        passwd = entry_passwd.get()
        v = Verificacion.verificar()
        if v.verificar(user, passwd):
            root.destroy()