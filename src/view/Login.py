import tkinter as tk
import tkinter.ttk as ttk
from controller.Verificador import Verificador

VER = Verificador()

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.user = None
        self.passwd = None
        self.open = True
        self.ventana("Iniciar Sesión", "INICIAR SESIÓN")

    def ventana(self, titulo="Ventana", texto="SAMPLE TEXT"):
        self.titulo = titulo
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

        # Formulario 1: Usuario
        frame1 = tk.Frame(self)

        labeluser = tk.Label(frame1, text="Usuario", font="Impact 11")
        self.userentry = ttk.Entry(frame1)
        labeluser.grid(row=0, column=0, sticky="w")
        self.userentry.grid(row=1, column=0, ipadx=25)

        frame1.pack(side="top", expand=True)

        # Formulario 2: Contraseña
        frame2 = tk.Frame(self)

        labelpasswd = tk.Label(frame2, text="Contraseña", font="Impact 11")
        self.passwdentry = ttk.Entry(frame2, show='*')
        labelpasswd.grid(row=0, column=0, sticky="w")
        self.passwdentry.grid(row=1, column=0, ipadx=25)

        frame2.pack(side="top", expand=True)

        # Boton
        # comando: command= lambda: Verificador.iniciarsesion(root, user, passwd)
        button = ttk.Button(self, text="Iniciar Sesión", command= lambda: VER.iniciarsesion(self, self.userentry, self.passwdentry))
        
        button.pack(side="top", expand=True, ipady=6, ipadx=10)

    def set_datos(self):
        self.user = self.userentry.get()
        self.passwd = self.passwdentry.get()

    def get_datos(self):
        return self.user, self.passwd

    def get_open(self):
        return self.open


