import tkinter as tk
import tkinter.ttk as ttk


# Clase contenedor
# Solo va a almacenar un Entry (campo para ingresar texto) y un Label (titulo del campo) dentro de un contenedor que despues se agrega a la ventana
class Contenedor:
    def __init__(self, root, texto):
        self.texto = texto
        self.frame = tk.Frame(root, pady=15, width=270, height=40)
        self.label = tk.Label(self.frame, text=texto, font=('Helvetica', 11))
        self.entry = ttk.Entry(self.frame, width=20, font=('Helvetica', 10))
        self.label.grid(sticky='w')
        self.entry.grid()

    def agregarFrame(self):
        self.frame.pack()


login = tk.Tk()

def closeWindow(bool):
    if (bool == True):
        login.destroy()
    return bool

# Aqui se añaden los componentes de la ventana
def showWindow(root):
    # Propiedades de la ventana
    ancho = 350
    alto = 400
    x = (login.winfo_screenwidth()//2)-(ancho//2)
    y = (login.winfo_screenheight()//2)-(alto//2)

    login.title("Iniciar Sesión")
    login.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
    login.resizable(False, False)

    # Etiquetas
    titulo = tk.Label(login,pady=15, text='INICIAR SESIÓN', font=('Impact', 18))
    titulo.pack()

    cont1 = Contenedor(login, "Usuario")
    cont1.agregarFrame()
    cont2 = Contenedor(login, "Contraseña")
    cont2.agregarFrame()
    cont3 = Contenedor(login, "Base de datos")
    cont3.agregarFrame()

    # Boton
    boton = ttk.Button(login, text="Iniciar Sesión", command= lambda: closeWindow(True))
    boton.pack(pady=15, ipadx=10, ipady=2)

    bool = closeWindow(False)
    if (bool == False):
        login.mainloop()


showWindow(login)
