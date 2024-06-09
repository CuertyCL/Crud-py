import tkinter as tk
import tkinter.ttk as ttk
from model.Verificacion import Verificacion

class Login(tk.Frame):
    def __init__(self, root):
        self.root = root
        super().__init__(root)
        self.pack(side="top", expand=True, fill="both")
        self.user = None
        self.passwd = None
        self.open = True
        

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
        button = ttk.Button(self, text="Iniciar Sesión", command=self.iniciarsesion)
        
        button.pack(side="top", expand=True, ipady=6, ipadx=10)

    def set_datos(self):
        self.user = self.userentry.get()
        self.passwd = self.passwdentry.get()

    def get_datos(self):
        return self.user, self.passwd

    def get_open(self):
        return self.open

    def iniciarsesion(self):
        self.set_datos()
        user, passwd = self.get_datos()
        v = Verificacion()
        if v.verificar(user, passwd):
            self.open = False

    


