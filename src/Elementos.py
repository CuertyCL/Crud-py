import tkinter as tk
import tkinter.ttk as ttk

# Clase Ventana
# Aqui se define el cómo sera la ventana para mostrar
class Ventana(tk.Tk):
    def __init__(self, texto=None):
        super().__init__()
        if texto is not None:
            self.texto = texto
            
        
    # Posición en pantalla al iniciar
    # La posicion de la ventana al iniciar será en el centro   
    def posicionVentana(self, ancho, alto):
        x = (self.winfo_screenwidth()//2)-(ancho//2)
        y = (self.winfo_screenheight()//2)-(alto//2)
        self.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))


    # Ventana que utiliza tanto el Login como el Menu Principal
    def menu(self, titulo, resizable=False, icono=None):
        self.posicionVentana(350, 430)
        if not resizable:
            self.resizable(False, False)

        # Titulo y Logo de la ventana
        self.title(titulo)
        if icono is not None:
            self.iconbitmap(icono)
        

    # Ventana donde se muestran las tablas de la DB
    def tablas(self, titulo, resizable=False, icono=None):
        self.posicionVentana(800, 600)
        if not resizable:
            self.resizable(False, False)

        # Titulo y Logo de la ventana
        self.title(titulo)
        if icono is not None:
            self.iconbitmap(icono)

        
    def emergente(self, titulo, resizable=False, icono=None):
        self.posicionVentana(800, 600)
        if not resizable:
            self.resizable(False, False)

        if icono is not None:
            self.iconbitmap(icono)


# Clase Contenedor
# Aqui se establecen como funciones el contenido de la ventana. Estos se agrupan
# dentro de un contenedor que despues se agrega a la ventana.
# Ideal en caso de que se tenga que repetir elementos.
class Contenedor:
    def __init__(self, root, texto=None):
        if texto is not None:
            self.texto = texto
        self.frame = tk.Frame(root, pady=9, width=270, height=40)

    # Encabezado
    def addTitulo(self):
        self.image = tk.PhotoImage(file="logo_sin_fondo_v2_128x128.png", width=128, height=128)
        self.label = ttk.Label(self.frame, image=self.image)
        self.titulo = tk.Label(self.frame, pady=9, text=self.texto, font=('Impact', 18))
        self.titulo.pack(pady=16)
        self.label.pack(side=tk.LEFT, padx=12)


    # Formularios
    def addFormulario(self):
        self.label = tk.Label(self.frame, text=self.texto, font=('Helvetica', 11))
        self.entry = ttk.Entry(self.frame, width=20, font=('Helvetica', 10))
        self.label.grid(sticky='w')
        self.entry.grid()

    def addDobleBoton(self, textoL, textoR):
        self.boton1 = ttk.Button(self.frame, text=textoL,padx=5, ipadx=10, ipady=2)
        self.boton2 = ttk.Button(self.frame, text=textoR,padx=5, ipadx=10, ipady=2)
        self.boton1.grid(side=tk.LEFT)
        self.boton2.grid(side=tk.RIGHT)

    def addFrame(self):
        self.frame.pack()