import tkinter as tk
import tkinter.ttk as ttk
import model.Consultas as con
import view.Componentes as comp

class Modificar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ventana(titulo="Modificar Stock", texto="MODIFICAR STOCK")

    def ventana(self, titulo="Ventana", texto="SAMPLE TEXT"):
        self.titulo = titulo
        self.texto = texto

        ancho = 900
        alto = 600

    # Posición en pantalla al iniciar
    # La posicion de la ventana al iniciar será en el centro  
        x = (self.winfo_screenwidth()//2)-(ancho//2)
        y = (self.winfo_screenheight()//2)-(alto//2)

        self.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
        self.resizable(False, False)

        self.title(titulo)

        # Divisiones de la Ventana
        

        self.add_contenido(self.texto)

    def add_contenido(self, texto):
        # Titulo y Logo
        frame0 = tk.Frame(self)
        self.image = tk.PhotoImage(file="./logo_128x128.png")
        labelimg = tk.Label(frame0, image=self.image)
        label = tk.Label(frame0, text=texto, font=("Impact", 24))
        labelimg.pack(side="left", expand=True)
        label.pack(side="left", expand=True)

        frame0.pack(side="top", expand=True)

        # Textos
        frame1 = tk.Frame(self)

        label1 = tk.Label(frame1, text="Texto de ejemplo numero 1 jajajajajajajaj")
        label1.pack(side="left")

        label2 = tk.Label(frame1, text="Texto de ejemplo numero 1")
        label2.pack(side="right")

        label3 = tk.Label(frame1, text="Texto de ejemplo numero 1")
        label3.pack(side="right")

        frame1.pack(side="top", expand=True, fill="both")

        # Tabla
        frame2 = comp.Componente()

        tabla = "inventario"

        consultas = con.Consultas("./db/inventario.db")
        data = consultas.get_data(tabla)
        head = consultas.get_title(tabla)

        frame2.create_table(head=head, data=data)
        
        frame2.pack(side='top', expand=True)

        # Botones 
        frame3 = tk.Frame(self)

        b_agregar = ttk.Button(frame3, text="Agregar Producto")
        b_opciones = comp.Componente()
        b_opciones.add_doble_boton("Aplicar Cambios", "Cancelar")


        b_agregar.pack(side='left', ipady=6, ipadx=10, padx=30, pady=10)
        b_opciones.pack(side='right', padx=20)

        frame3.pack(side='top', expand=True, fill='both')

if __name__ == "__main__":
    root = Modificar()
    root.mainloop()