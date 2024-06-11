from view.Login import Login
from view.Inicio import Inicio
from view.Agregar import Añadir


class Abrir():
    def __init__(self):
        pass

    def abrir_login():
        login = Login()
        login.mainloop()

    def abrir_opciones():
        pass

    def abrir_menu():
        inicio = Inicio()
        inicio.mainloop()

    def abrir_inventario():
        pass

    def abrir_añadir_inventario():
        añadir = Añadir()
        añadir.mainloop()

    def abrir_eliminar_inventario():
        pass

    def abrir_añadir_producto():
        pass