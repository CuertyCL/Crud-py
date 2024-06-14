import tkinter as tk
import tkinter.ttk as ttk
from almacen.Verificador import Verificador
import view.Componentes as comp

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

        ancho = 360
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
        frame1 = comp.Componente()
        frame1.add_triple_boton(text1="Opciones",
                                text2="Cerrar Sesión",
                                text3="Salir",
                                comm1=self.destroy,
                                comm2=self.destroy,
                                comm3=self.destroy,
                                padx=10)

        frame1.pack(side="top", expand=True)

if __name__ == "__main__":
    root = Inicio()
    root.mainloop()