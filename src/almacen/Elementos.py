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
class Contenedor(tk.Frame):
    def __init__(self, root, pady=None, width=None, height=None):
        if pady is not None:
            self.pady = pady
        else:
            self.pady = 9

        if pady is not None:
            self.width = width
        else:
            self.witdh = 270

        if pady is not None:
            self.height = height
        else:
            self.height = 40

        super().__init__(root, pady=pady, width=width, height=height)
        

    # Encabezado
    def addTitulo(self, texto, icono):
        self.image = tk.PhotoImage(file=icono, width=128, height=128)
        self.label = ttk.Label(self, image=self.image)
        self.titulo = tk.Label(self, pady=6, text=texto, font=('Impact', 18))
        self.label.grid(row=1, column=1, sticky='w', padx=12)
        self.titulo.grid(row=1, column=2, sticky='e', pady=16)


    # Formularios
    def addFormulario(self, texto):
        self.label = tk.Label(self, text=texto, font=('Helvetica', 11))
        self.entry = ttk.Entry(self, width=20, font=('Helvetica', 10))
        self.label.grid(sticky='w')
        self.entry.grid()

    # Botones
    def addDobleBoton(self, textoL, textoR):
        self.boton1 = ttk.Button(self, text=textoL)
        self.boton2 = ttk.Button(self, text=textoR)
        self.boton1.grid(row=1, column=1, sticky='e', padx=14, ipadx=10, ipady=2)
        self.boton2.grid(row=1, column=2, sticky='w', padx=22, ipadx=10, ipady=2)

    def addFrame(self, after=None, before=None, pady=0):
        if after is None and before is None:
            self.pack(pady=pady)
        elif after is not None and before is None:
            self.pack(after=after, pady=pady)
        elif after is None and before is not None:
            self.pack(before=before, pady=pady)