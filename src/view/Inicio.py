import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msbox
from almacen.Verificador import Verificador
import view.Componentes as comp
import controller.Abrir as abrir


VER = Verificador()

class Inicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana("Menu Inicio", "MENÚ")

    def ventana(self, titulo=None, texto=None):
        if titulo is None: self.titulo = "Ventana"
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
        b1 = ttk.Button(self, text="Ver\nInventario", command=self.abrir_inventario)
        b1.pack(side="top", expand=True, ipady=6, ipadx=20)

        b2 = ttk.Button(self, text="Modificar\nStock", command=self.abrir_modificar)
        b2.pack(side="top", expand=True, ipady=6, ipadx=20)

        b3 = ttk.Button(self, text="Añadir\nProducto", command=self.abrir_añadir_inventario)
        b3.pack(side="top", expand=True, ipady=6, ipadx=20)

        b4 = ttk.Button(self, text="Eliminar\nProducto", command=self.abrir_eliminar_inventario)
        b4.pack(side="top", expand=True, ipady=6, ipadx=20)

        # Botones Opciones y Cerrar Sesión
        frame1 = comp.Componente()
        frame1.add_triple_boton(text1="Opciones",
                                text2="Cerrar Sesión",
                                text3="Salir",
                                comm1=self.abrir_opciones,
                                comm2=self.cerrar_sesion,
                                comm3=self.cerrar_ventana,
                                padx=10)

        frame1.pack(side="top", expand=True)


    def abrir_añadir_inventario(self):
        self.destroy()
        abrir.Abrir.abrir_añadir_inventario()

    def abrir_eliminar_inventario(self):
        self.destroy()
        abrir.Abrir.abrir_eliminar_inventario()

    def abrir_modificar(self):
        self.destroy()
        abrir.Abrir.abrir_modificar_stock()

    def abrir_inventario(self):
        self.destroy()
        abrir.Abrir.abrir_inventario()

    def abrir_opciones(self):
        abrir.Abrir.abrir_opciones(self)
    
    def cerrar_sesion(self):
        self.destroy()
        abrir.Abrir.abrir_login()

    def cerrar_ventana(self):
        respuesta = msbox.askokcancel("Salir", "¿Seguro que quieres salir?")
        if respuesta:
            self.destroy()


if __name__ == "__main__":
    root = Inicio()
    root.mainloop()
