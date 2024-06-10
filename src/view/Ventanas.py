import tkinter as tk
import tkinter.ttk as ttk

# Clase Ventana
# Aqui se define el cómo sera la ventana para mostrar
class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ventana_inicio("Iniciar Sesión", )

    # Ventana tanto para el login como para el
    # menu de inicio. Tambien puede servir para otras ventanas
    def ventana_inicio(self, titulo=None, texto=None):
        if titulo is None:
            self.titulo = "Ventana"
        else:
            self.titulo = titulo

        if texto is None:
            self.texto = "SAMPLE TEXT"
        else:
            self.texto = texto

        ancho = 350
        alto = 430

    # Posición en pantalla al iniciar
    # La posicion de la ventana al iniciar será en el centro  
        x = (self.winfo_screenwidth()//2)-(ancho//2)
        y = (self.winfo_screenheight()//2)-(alto//2)

        self.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
        self.resizable(False, False)

        self.title(titulo)

    def ventana_tablas(self, titulo):
        ancho = 1024
        alto = 768
        x = (self.winfo_screenwidth()//2)-(ancho//2)
        y = (self.winfo_screenheight()//2)-(alto//2)
        self.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
        self.minsize("800x600")

        self.title(titulo)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure(1, weight=4)
