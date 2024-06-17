import tkinter as tk
import tkinter.ttk as ttk
import model.Consultas as con
import view.Componentes as comp
import controller.Abrir as abrir

class Inventario(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.add_ventana()

    def add_ventana(self):
        ancho = 1024
        alto = 768
        x = (self.winfo_screenwidth()//2)-(ancho//2)
        y = (self.winfo_screenheight()//2)-(alto//2)
        self.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))

        self.title("Inventario")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.rowconfigure((0, 2), weight=1)
        self.rowconfigure(1, weight=4)
        self.add_contenido()

    def add_contenido(self):

        # Logo y titulo
        image = tk.PhotoImage(file="./logo_128x128.png")
        labelimg = tk.Label(self, image=image)
        label = tk.Label(self, text="INVENTARIO", font=("Impact", 24))

        labelimg.grid(row=0, column=0, sticky="nw")
        label.grid(row=0, column=0, sticky="ne", pady=50)


        # Lista de productos
        tabla = "inventario"
        consultas = con.Consultas("./db/inventario.db")
        head = consultas.get_title(tabla)
        head.insert(0, "-- Selecciona una Columna --")

        combo = ttk.Combobox(self, values=head)
        combo.current(0)

        combo.grid(row=0, column=1)

        # Botones de filtrado
        fbotones = tk.Frame(self, highlightbackground="gray", highlightthickness=4)
        fbotones.grid(row=1, column=0, sticky="nsew", padx=15, pady=15)

        b1 = ttk.Button(fbotones, text="Ver Todas\nlas Tablas")
        b1.pack(side="top", expand=True, ipady=6, ipadx=10)

        b2 = ttk.Button(fbotones, text="Filtrar")
        b2.pack(side="top", expand=True, ipady=6, ipadx=10)

        b3 = ttk.Button(fbotones, text="Generar\nLista")
        b3.pack(side="top", expand=True, ipady=6, ipadx=10)

        b4 = ttk.Button(fbotones, text="Enviar Lista\nal Correo")
        b4.pack(side="top", expand=True, ipady=6, ipadx=10)


        # Contenedor para la tabla
        ftabla_wrapper = tk.Frame(self)
        ftabla_wrapper.grid(row=1, column=1, sticky="nsew", padx=15, pady=15)

        # Tabla
        ftabla = comp.Componente(ftabla_wrapper)  # Pasar ftabla_wrapper como padre

        tabla = "inventario"
        head = consultas.get_title(tabla)
        data = consultas.get_data(tabla)

        ftabla.create_table(head=head, data=data, side='right')  # Posiciona la tabla a la derecha

        ftabla.pack(expand=True, fill='both')


        # Boton Volver
        bsalir = ttk.Button(self, text="Volver", command=self.cerrar_ventana)
        bsalir.grid(row=2, column=0, ipady=6, ipadx=10)

    def cerrar_ventana(self):
        self.destroy()
        abrir.Abrir.abrir_menu()


