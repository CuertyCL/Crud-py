import tkinter as tk
import tkinter.ttk as ttk
import view.Componentes as comp
import model.Verificacion as ver

VER = ver.Verificacion()

class Opciones(tk.Toplevel):
    def __init__(self, root=None):
        super().__init__(root)
        self.ventana()

    def ventana(self, titulo="Opciones", texto="OPCIONES"):
        self.title(titulo)

        ancho = 500
        alto = 300

        # Posición en pantalla al iniciar
        # La posicion de la ventana al iniciar será en el centro  
        x = (self.winfo_screenwidth()//2)-(ancho//2)
        y = (self.winfo_screenheight()//2)-(alto//2)

        self.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
        self.resizable(False, False)

        self.resizable(False, False)
        self.add_contenido(texto)

    def add_contenido(self, titulo):
        # Titulo y Logo
        frame0 = tk.Frame(self)
        self.image = tk.PhotoImage(file="./logo_128x128.png")
        labelimg = tk.Label(frame0, image=self.image)
        label = tk.Label(frame0, text=titulo, font=("Impact", 24))
        labelimg.pack(side="left", expand=True)
        label.pack(side="left", expand=True)

        frame0.pack(side="top", expand=True)
        
        # Datos de usuario
        frame1 = tk.Frame(self)

        label_nombre_usuario = tk.Label(frame1, text="Nombre de\nUsuario")
        label_user = tk.Label(frame1, text=VER.get_nombre())
        botones = comp.Componente(frame1)
        botones.add_doble_boton(text1="Cambiar\nNombre",
                                text2="Cambiar\nContraseña")
        
        label_nombre_usuario.pack(side="left", expand=True)
        label_user.pack(side="left", expand=True)
        botones.pack(side="left", expand=True)

        frame1.pack(side='top', expand=True, fill='both')

        # Boton Volver
        frame2 = tk.Frame(self)

        b_volver = ttk.Button(frame2, text="Volver", command=self.destroy)
        b_volver.pack(side='right', ipady=6, ipadx=10, padx=30)

        frame2.pack(side='top', expand=True, fill='both')
    


if __name__ == "__main__":
    op = Opciones()
    op.mainloop()