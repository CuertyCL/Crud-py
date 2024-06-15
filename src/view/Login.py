import tkinter as tk
import tkinter.ttk as ttk
import controller.Abrir as abrir
import model.Verificacion as ver

VER =ver.Verificacion()

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.user = None
        self.passwd = None
        self.open = True
        self.label_error_user = None
        self.label_error_passwd = None
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

        # Botón para mostrar/ocultar contraseña
        show_password = tk.BooleanVar()
        show_button = ttk.Checkbutton(frame2, text="Mostrar Contraseña", variable=show_password, command= lambda: self.ver_passwd(show_password))
        show_button.grid(row=2, column=0, padx=10, sticky='w')
        
        frame2.pack(side="top", expand=True)


        # Boton Iniciar Sesión
        button = ttk.Button(self, text="Iniciar Sesión", command= lambda: self.iniciar_sesion(frame1, frame2, self.userentry, self.passwdentry))
        
        button.pack(side="top", expand=True, ipady=6, ipadx=10)

    def iniciar_sesion(self, frame1, frame2, userentry, passwdentry):
        user = userentry.get()
        passwd = passwdentry.get()

        isuser = False
        ispasswd = False
        isadmin = False

        isuser, ispasswd, isadmin= VER.verificar(usuario=user, contraseña=passwd)

        if self.label_error_user:
            self.label_error_user.grid_forget()
            self.label_error_user = None

        if self.label_error_passwd:
            self.label_error_passwd.grid_forget()
            self.label_error_passwd = None

        if isuser and ispasswd:
            self.destroy()
            if isadmin:
                abrir.Abrir.abrir_menu()
            else:
                abrir.Abrir.abrir_menu_user()
        elif isuser and not ispasswd:
            self.label_error_passwd = tk.Label(frame2, text="Contraseña incorrecta.\nVerifique que escribió bien la contraseña", fg="red")
            self.label_error_passwd.grid(row=2, column=0, pady=10)
        else:
            self.label_error_user = tk.Label(frame1, text="Usuario incorrecto.\nVerifique que escribió bien el usuario.", fg="red")
            self.label_error_user.grid(row=2, column=0, pady=10)


    def ver_passwd(self, show_passwd):
        if show_passwd.get():
            self.passwdentry.config(show="")
        else:
            self.passwdentry.config(show="*")


