import tkinter as tk
import tkinter.ttk as ttk
import view.Componentes as comp

class Añadir(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ventana("Añadir Producto", "AÑADIR\nPRODUCTO")

    def ventana(self, titulo=None, texto=None):
        if titulo is None:
            self.titulo = "Ventana"
        else:
            self.titulo = titulo

        if texto is None:
            self.texto = "SAMPLE TEXT"
        else:
            self.texto = texto

        ancho = 450
        alto = 786

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

        # Formulario 1: Nombre
        frame1 = comp.Componente()
        frame1.add_formulario(titulo="Nombre")
        frame1.pack(side="top", expand=True)

        # Formulario 2: Clase
        frame2 = comp.Componente()
        frame2.add_lista(titulo="Clase")
        frame2.pack(side="top", expand=True)

        # Formulario 3: Lugar de Compra
        frame3 = comp.Componente()
        frame3.add_lista(titulo="Lugar de Compra")
        frame3.pack(side="top", expand=True)

        # Formulario 4: Precio
        frame4 = comp.Componente()
        frame4.add_formulario(titulo="Precio")
        frame4.pack(side="top", expand=True)

        # Formulario 5: Unidad
        frame5 = comp.Componente()
        frame5.add_lista(titulo="Unidad")
        frame5.pack(side="top", expand=True)

        # Formulario 6: Stock Disponible
        frame6 = comp.Componente()
        frame6.add_formulario(titulo="Stock Disponible")
        frame6.pack(side="top", expand=True)

        # Formulario 7: Stock Maximo
        frame7 = comp.Componente()
        frame7.add_formulario(titulo="Stock Maximo")
        frame7.pack(side="top", expand=True)

        # Formulario 8: Stock Minimo
        frame8 = comp.Componente()
        frame8.add_formulario(titulo="Stock Minimo")
        frame8.pack(side="top", expand=True)

        # Botones
        botones = comp.Componente()
        botones.add_triple_boton("Ver Inventario", "Confirmar", "Cancelar", comm1=self.destroy, comm2=self.destroy, comm3=self.destroy)
        botones.pack(side="top", expand=True)
        

if __name__ == "__main__":
    root = Añadir()
    root.mainloop()