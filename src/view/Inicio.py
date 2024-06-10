import tkinter as tk
import tkinter.ttk as ttk
from controller.Verificador import Verificador

VER = Verificador()

class Inicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ventana("Menu Inicio", "MENÚ")
        


    def ventana(self, titulo=None, texto=None):
        if titulo is None:
            self.titulo = "Ventana"
        else:
            self.titulo = titulo

        if texto is None:
            self.texto = "SAMPLE TEXT"
        else:
            self.texto = texto

        ancho = 350
        alto = 460

    # Posición en pantalla al iniciar
    # La posicion de la ventana al iniciar será en el centro  
        x = (self.winfo_screenwidth()//2)-(ancho//2)
        y = (self.winfo_screenheight()//2)-(alto//2)

        self.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
        self.resizable(False, False)

        self.title(titulo)
        self.add_contenido(self.texto)

    def add_contenido(self, titulo):
        # Titulo y Logo
        frame0 = tk.Frame(self)
        self.image = tk.PhotoImage(file="./logo_128x128.png")
        labelimg = tk.Label(frame0, image=self.image)
        label = tk.Label(frame0, text=titulo, font=("Impact", 24))
        labelimg.pack(side="left", expand=True)
        label.pack(side="left", expand=True)

        frame0.pack(side="top", expand=True)

        # Botones
        b1 = ttk.Button(self, text="Ver\nInventario", command= lambda: VER.cerrar_ventana(self))
        b1.pack(side="top", expand=True, ipady=6, ipadx=20)

        b2 = ttk.Button(self, text="Modificar\nStock", command= lambda: VER.cerrar_ventana(self))
        b2.pack(side="top", expand=True, ipady=6, ipadx=20)

        b3 = ttk.Button(self, text="Añadir\nProducto", command= lambda: VER.cerrar_ventana(self))
        b3.pack(side="top", expand=True, ipady=6, ipadx=20)

        b4 = ttk.Button(self, text="Eliminar\nProducto", command= lambda: VER.cerrar_ventana(self))
        b4.pack(side="top", expand=True, ipady=6, ipadx=20)

        # Botones Opciones y Cerrar Sesión
        frame1 = tk.Frame(self)
        b_op = ttk.Button(frame1, text="Opciones", command= lambda: VER.cerrar_ventana(self))
        b_cs = ttk.Button(frame1, text="Cerrar Sesión", command= lambda: VER.cerrar_ventana(self))

        b_op.pack(side="left", expand=True, ipady=6, ipadx=10, padx=20, pady=10)
        b_cs.pack(side="left", expand=True, ipady=6, ipadx=10, padx=20, pady=10)

        frame1.pack(side="top", expand=True)

if __name__ == "__main__":
    root = Inicio()
    root.mainloop()