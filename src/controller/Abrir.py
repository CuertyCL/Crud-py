from view.Login import Login
from view.Inicio import Inicio
from view.Agregar import Añadir
from view.Opciones import Opciones
from view.Modificar import Modificar
from view.Inventario import Inventario
from view.Inicio_user import InicioUser

class Abrir():
    def __init__(self):
        pass

    def abrir_login():
        login = Login()

    def abrir_opciones(root):
        opciones = Opciones(root)

    def abrir_menu():
        inicio = Inicio()

    def abrir_menu_user():
        inicio_user = InicioUser()

    def abrir_inventario():
        inventario = Inventario()

    def abrir_modificar_stock():
        modificar = Modificar()

    def abrir_añadir_inventario():
        añadir = Añadir()
        

    def abrir_eliminar_inventario():
        pass

    def abrir_añadir_producto():
        pass
