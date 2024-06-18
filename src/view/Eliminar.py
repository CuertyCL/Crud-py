import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msbox
import view.Componentes as comp
import model.Consultas as con
import controller.Abrir

CONSULTAS = con.Consultas("./db/inventario.db")

class Eliminar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.ventana("Eliminar Producto", "ELIMINAR PRODUCTO")

    def ventana(self, titulo="Ventana", texto="SAMPLE TEXT"):
        self.titulo = titulo
        self.texto = texto

        ancho = 500
        alto = 500

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

        # Texto indicando que debe elegir qué producto
        # quiere eliminar
        frame1 = tk.Frame(self)

        label_eliminar = tk.Label(frame1, text="Elige un proucto para eliminarlo del inventario.", font="Impact")
        label_aviso = tk.Label(frame1, text="Recuerda que esta acción no se puede deshacer.", font="Impact")
        label_eliminar.pack(side='top', expand=True)
        label_aviso.pack(side='top', expand=True)

        frame1.pack(side='top', expand=True)

        # Lista de los productos
        self.frame2 = comp.Componente()
        values_productos = CONSULTAS.get_data(table="inventario",
                                          column="nombre",
                                          specify_column=True,
                                          index=0)

        self.frame2.add_lista(titulo="Productos",
                              values=values_productos,
                              default="-- Selecciona un Producto --")
        self.frame2.combobox.bind("<<ComboboxSelected>>", lambda event: self.mostrar_datos(self.frame2.get_selected_list()))
        
        self.frame2.pack(side='top', expand=True)

        # Datos del Producto
        self.frame3 = tk.Frame(self)

        self.frame3.columnconfigure((0,1), weight=1)

        # Titulos
        self.titulo_nombre = tk.Label(self.frame3, text="Nombre: ", font="Impact")
        self.titulo_clase = tk.Label(self.frame3, text="Clase: ", font="Impact")
        self.titulo_lugar = tk.Label(self.frame3, text="Lugar de Compra: ", font="Impact")
        self.titulo_unidad = tk.Label(self.frame3, text="Unidad: ", font="Impact")
        self.titulo_precio = tk.Label(self.frame3, text="Precio: ", font="Impact")
        self.titulo_stock_min = tk.Label(self.frame3, text="Stock Minimo: ", font="Impact")
        self.titulo_stock_max = tk.Label(self.frame3, text="Stock Maximo: ", font="Impact")
        self.titulo_stock = tk.Label(self.frame3, text="Stock Disponible: ", font="Impact")

        self.titulo_nombre.grid(row=0, column=0, sticky='w')
        self.titulo_clase.grid(row=1, column=0, sticky='w')
        self.titulo_lugar.grid(row=2, column=0, sticky='w')
        self.titulo_unidad.grid(row=3, column=0, sticky='w')
        self.titulo_precio.grid(row=4, column=0, sticky='w')
        self.titulo_stock_min.grid(row=5, column=0, sticky='w')
        self.titulo_stock_max.grid(row=6, column=0, sticky='w')
        self.titulo_stock.grid(row=7, column=0, sticky='w')
    
        # Datos
        self.dato_nombre = tk.Label(self.frame3, text="", font="Impact")
        self.dato_clase = tk.Label(self.frame3, text="", font="Impact")
        self.dato_lugar = tk.Label(self.frame3, text="", font="Impact")
        self.dato_unidad = tk.Label(self.frame3, text="", font="Impact")
        self.dato_precio = tk.Label(self.frame3, text="", font="Impact")
        self.dato_stock_min = tk.Label(self.frame3, text="", font="Impact")
        self.dato_stock_max = tk.Label(self.frame3, text="", font="Impact")
        self.dato_stock = tk.Label(self.frame3, text="", font="Impact")

        self.dato_nombre.grid(row=0, column=1, sticky='e')
        self.dato_clase.grid(row=1, column=1, sticky='e')
        self.dato_lugar.grid(row=2, column=1, sticky='e')
        self.dato_unidad.grid(row=3, column=1, sticky='e')
        self.dato_precio.grid(row=4, column=1, sticky='e')
        self.dato_stock_min.grid(row=5, column=1, sticky='e')
        self.dato_stock_max.grid(row=6, column=1, sticky='e')
        self.dato_stock.grid(row=7, column=1, sticky='e')

        self.frame3.pack(side='top', expand=True)

        # Botones
        self.frame4 = comp.Componente()
        self.frame4.add_doble_boton(side='right',
                                    text1="Aplicar",
                                    text2="Cancelar",
                                    comm1=self.aplicar_cambios,
                                    comm2=self.cerrar_ventana)
        self.frame4.pack(side='top', expand=True)

    def cerrar_ventana(self) -> None:
        self.destroy()
        controller.Abrir.Abrir.abrir_menu()

    def mostrar_datos(self, nombre) -> None:
        datos = CONSULTAS.get_specific_data(table="inventario", column="nombre", name=nombre)

        clase = CONSULTAS.get_name_from_id(table="clases", column="id_clase", id=datos[2])
        lugar = CONSULTAS.get_name_from_id(table="lugares", column="id_lugar", id=datos[3])
        unidad = CONSULTAS.get_name_from_id(table="unidades", column="id_unidad", id=datos[4])
        
        self.dato_nombre.config(text=f"{datos[1]}", font="Impact")
        self.dato_clase.config(text=f"{clase}", font="Impact")
        self.dato_lugar.config(text=f"{lugar}", font="Impact")
        self.dato_unidad.config(text=f"{unidad}", font="Impact")
        self.dato_precio.config(text=f"${datos[5]}", font="Impact")
        self.dato_stock_min.config(text=f"{datos[6]}", font="Impact")
        self.dato_stock_max.config(text=f"{datos[7]}", font="Impact")
        self.dato_stock.config(text=f"{datos[8]}", font="Impact")

    def aplicar_cambios(self) -> None:
        message = msbox.askquestion("¿Aplicar Cambios?", "¿Desea Eliminar este Producto?\nEsta acción no se podrá deshacer.")
        if message=="yes":
            self.eliminar_datos()
            msbox.showinfo("Datos Eliminados", "¡Se han eliminado los datos correctamente!")
        else:
            pass
    
    def eliminar_datos(self) -> None:
        producto = self.frame2.get_selected_list()
        CONSULTAS.delete_record(column="nombre", table="inventario", where=producto)



if __name__ =="__main__":
    root = Eliminar()
    root.mainloop()