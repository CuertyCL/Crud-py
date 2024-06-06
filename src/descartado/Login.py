import tkinter as tk
import tkinter.ttk as ttk
import Elementos as cont
#import sqlite3

login = tk.Tk()

def closeWindow(bool):
    if bool:
        login.destroy()
    return bool

# Aqui se añaden los componentes de la ventana
def showWindow(root):
    # Propiedades de la ventana
    ancho = 350
    alto = 430
    x = (login.winfo_screenwidth()//2)-(ancho//2)
    y = (login.winfo_screenheight()//2)-(alto//2)

    root.title("Iniciar Sesión")
    root.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
    root.resizable(False, False)
    root.iconbitmap('logo.ico')

    # Etiquetas

    encabezado = cont.Contenedor(root, "INICIAR SESIÓN")
    encabezado.addTitulo()
    encabezado.addFrame()

    cont1 = cont.Contenedor(root, "Usuario")
    cont1.addFormulario()
    cont1.addFrame()
    cont2 = cont.Contenedor(root, "Contraseña")
    cont2.addFormulario()
    cont2.addFrame()

    # Boton
    boton = ttk.Button(root, text="Iniciar Sesión", command= lambda: closeWindow(True))
    boton.pack(pady=20, ipadx=10, ipady=2)

    bool = closeWindow(False)
    while not bool:
        login.mainloop()


showWindow(login)
