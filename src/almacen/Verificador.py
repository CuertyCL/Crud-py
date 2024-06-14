from model.Verificacion import Verificacion
import tkinter as tk

class Verificador:

    valid = False
    open = True

    def __init__(self):
        pass

    def iniciarsesion(self, frame1, frame2, entry_user, entry_passwd):
        isuser = False
        ispasswd = False

        user = entry_user.get()
        passwd = entry_passwd.get()
        isuser, ispasswd = Verificacion.verificar(usuario=user, contraseña=passwd)
        if self.label_error_user:
            self.label_error_user.grid_forget()
            self.label_error_user = None

        if self.label_error_passwd:
            self.label_error_passwd.grid_forget()
            self.label_error_passwd = None

        if isuser and ispasswd:
            self.root.destroy()
        elif isuser and not ispasswd:
            self.label_error_passwd = tk.Label(frame2, text="Contraseña incorrecta.\nVerifique que escribió bien la contraseña", fg="red")
            self.label_error_passwd.grid(row=2, column=0, pady=10)
        else:
            self.label_error_user = tk.Label(frame1, text="Usuario incorrecto.\nVerifique que escribió bien el usuario.", fg="red")
            self.label_error_user.grid(row=2, column=0, pady=10)
        

    def get_valid(self):
        return self.valid

    def cerrar_ventana(self, root):
        root.destroy()

            
VER = Verificador()