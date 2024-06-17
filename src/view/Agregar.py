import tkinter as tk
import tkinter.messagebox as msbox
import tkinter.ttk as ttk
import view.Componentes as comp
import controller.Abrir
import model.Consultas as con

CONSULTAS = con.Consultas("./db/inventario.db")

class Añadir(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
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
        #self.resizable(False, False)
        self.resizable(True, True)

        self.title(titulo)
        self.add_contenido(self.texto)

    def add_contenido(self, titulo):
        # Titulo y Logo
        self.frame0 = tk.Frame(self)
        self.image = tk.PhotoImage(file="./logo_128x128.png")
        self.labelimg = tk.Label(self.frame0, image=self.image)
        self.label = tk.Label(self.frame0, text=titulo, font=("Impact", 24))
        self.labelimg.pack(side="left", expand=True)
        self.label.pack(side="left", expand=True)

        self.frame0.pack(side="top", expand=True)

        # Formulario 1: Nombre
        self.frame1 = comp.Componente()
        self.frame1.add_formulario(titulo="Nombre")
        self.frame1.pack(side="top", expand=True)

        # Formulario 2: Clase
        self.frame2 = comp.Componente()
        values_clase = CONSULTAS.get_data(table="clases", column="nombre_clase", specify_column=True, index=0)
        self.frame2.add_lista(titulo="Clase", values=values_clase, default="-- Selecciona una clase --")
        self.frame2.pack(side="top", expand=True)

        # Formulario 3: Lugar de Compra
        # self.frame3 = comp.Componente()
        # self.frame3.add_lista(titulo="Lugar de Compra", default="-- Selecciona un Lugar de Compra --")
        # self.frame3.pack(side="top", expand=True)

        # Formulario 4: Precio
        self.frame4 = comp.Componente()
        self.frame4.add_formulario(titulo="Precio")
        self.frame4.pack(side="top", expand=True)

        # Formulario 5: Unidad
        # self.frame5 = comp.Componente()
        # self.frame5.add_lista(titulo="Unidad")
        # self.frame5.pack(side="top", expand=True)

        # Formulario 6: Stock Disponible
        self.frame6 = comp.Componente()
        self.frame6.add_formulario(titulo="Stock Disponible")
        self.frame6.pack(side="top", expand=True)

        # Formulario 7: Stock Maximo
        # self.frame7 = comp.Componente()
        # self.frame7.add_formulario(titulo="Stock Maximo")
        # self.frame7.pack(side="top", expand=True)

        # Formulario 8: Stock Minimo
        self.frame8 = comp.Componente()
        self.frame8.add_formulario(titulo="Stock Minimo")
        self.frame8.pack(side="top", expand=True)

        # Botones
        self.botones = comp.Componente()
        self.botones.add_triple_boton("Ver Inventario",
                                 "Confirmar",
                                 "Cancelar",
                                 comm1=self.destroy,
                                 comm2=self.aplicar_cambios,
                                 comm3=self.cerrar_ventana)
        self.botones.pack(side="top", expand=True)
        
    def cerrar_ventana(self):
        self.destroy()
        controller.Abrir.Abrir.abrir_menu()

    def aplicar_cambios(self):
        message = msbox.askquestion("¿Aplicar Cambios?", "¿Desea ingresar los datos?")
        if message=="yes":
            self.insertar_datos()
            msbox.showinfo("Datos Ingresados", "¡Se han ingresado los datos correctamente!")
        else:
            pass

    def insertar_datos(self):
        nombre = self.frame1.get_entry()
        clase = CONSULTAS.get_id_from_column(name=self.frame2.get_selected_list(), table="clases", column="nombre_clase")
        precio = self.frame4.get_entry()
        stock_d = self.frame6.get_entry()
        stock_min = self.frame8.get_entry()

        CONSULTAS.insert_data_inventario(nombre, clase, precio, stock_d, stock_min)

        






if __name__ == "__main__":
    root = Añadir()
    root.mainloop()
