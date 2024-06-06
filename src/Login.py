import tkinter as tk
import tkinter.ttk as ttk

USER = "usuario"
PASSWD = "contraseña"

def iniciarsesion(root, entry_user, entry_passwd):
    user = entry_user.get()
    passwd = entry_passwd.get()
    if user==USER and passwd==PASSWD:
        root.destroy()

root = tk.Tk()
ancho = 350
alto = 430
x = (root.winfo_screenwidth()//2)-(ancho//2)
y = (root.winfo_screenheight()//2)-(alto//2)

root.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
root.resizable(False, False)

# Titulo y Logo
frame1 = tk.Frame(root)

image =tk. PhotoImage(file="./logo_128x128.png")
labelimg = tk.Label(frame1, image=image)
label = tk.Label(frame1, text="INICIAR SESIÓN", font=("Impact", 24))
labelimg.pack(side="left", expand=True)
label.pack(side="left", expand=True)

frame1.pack(side="top", expand=True)

# Formulario 1
frame2 = tk.Frame(root)

labeluser = tk.Label(frame2, text="Usuario", font="Helvetica 11")
user = ttk.Entry(frame2)
labeluser.grid(row=0, column=0, sticky="w")
user.grid(row=1, column=0, ipadx=25)

frame2.pack(side="top", expand=True)

# Formulario 2
frame3 = tk.Frame(root)

labelpasswd = tk.Label(frame3, text="Contraseña", font="Helvetica 11")
passwd = ttk.Entry(frame3, show='*')
labelpasswd.grid(row=0, column=0, sticky="w")
passwd.grid(row=1, column=0, ipadx=25)

frame3.pack(side="top", expand=True)

# Boton
button = ttk.Button(root, text="Iniciar Sesión", command= lambda: iniciarsesion(root, user, passwd))
button.pack(side="top", expand=True, ipady=6, ipadx=10)


root.mainloop()
