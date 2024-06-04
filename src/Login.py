import tkinter as tk
import tkinter.ttk as ttk

# Clase contenedor
# Solo va a almacenar un Entry (campo para ingresar texto) y un Label (titulo del campo)
# dentro de un contenedor que despues se agrega a la ventana
class Contenedor:
    def __init__(self, root, texto):
        self.texto = texto
        self.frame = tk.Frame(root, pady=10, width=270, height=40)


    def addTitle(self):
        self.image = tk.PhotoImage(file="imagen_sin_fondo.png", width=100, height=100)
        self.label = ttk.Label(self.frame, image=self.image)
        self.titulo = tk.Label(self.frame, pady=15, text='INICIAR SESIÓN', font=('Impact', 18))
        self.label.pack(side=tk.LEFT, padx=12)
        self.titulo.pack(pady=16)


    def addLabelEntry(self):
        self.label = tk.Label(self.frame, text=self.texto, font=('Helvetica', 11))
        self.entry = ttk.Entry(self.frame, width=20, font=('Helvetica', 10))
        self.label.grid(sticky='w')
        self.entry.grid()

    def addFrame(self):
        self.frame.pack()


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

    # Etiquetas

    encabezado = Contenedor(root, "INICIAR SESIÓN")
    encabezado.addTitle()
    encabezado.addFrame()

    cont1 = Contenedor(root, "Usuario")
    cont1.addLabelEntry()
    cont1.addFrame()
    cont2 = Contenedor(root, "Contraseña")
    cont2.addLabelEntry()
    cont2.addFrame()
    cont3 = Contenedor(root, "Base de datos")
    cont3.addLabelEntry()
    cont3.addFrame()

    # Boton
    boton = ttk.Button(root, text="Iniciar Sesión", command= lambda: closeWindow(True))
    boton.pack(pady=20, ipadx=10, ipady=2)

    bool = closeWindow(False)
    if not bool:
        login.mainloop()


showWindow(login)
