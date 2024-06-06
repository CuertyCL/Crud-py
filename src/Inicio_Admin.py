import tkinter as tk
import tkinter.ttk as ttk


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
label = tk.Label(frame1, text="INICIO", font=("Impact", 24))
labelimg.pack(side="left", expand=True)
label.pack(side="left", expand=True)

frame1.pack(side="top", expand=True)

# Boton Tablas
button = ttk.Button(root, text="Ver Tablas", command=root.destroy)
button.pack(side="top", expand=True, ipady=6, ipadx=10)

# Doble Boton 1
frame2 = tk.Frame(root)

frame2.columnconfigure((0,1), weight=1)

button1 = ttk.Button(frame2, text="Modificar\nStock", command=root.destroy)
button2 = ttk.Button(frame2, text="Modificar\nInventario", command=root.destroy)
button1.grid(row=0, column=0, ipady=6, ipadx=10)
button2.grid(row=0, column=1, ipady=6, ipadx=10)

frame2.pack(side="top", expand=True, fill='x')

# Doble Boton 1
frame3 = tk.Frame(root)

frame3.columnconfigure((0,1), weight=1)

button3 = ttk.Button(frame3, text="Añadir\nVenta", command=root.destroy)
button4 = ttk.Button(frame3, text="Modificar\nMenu", command=root.destroy)
button3.grid(row=0, column=0, ipady=6, ipadx=10)
button4.grid(row=0, column=1, ipady=6, ipadx=10)

frame3.pack(side="top", expand=True, fill='x')

# Boton Eliminar
frame4 = tk.Frame(root)

frame4.columnconfigure((0,1), weight=1, uniform='a')

button5 = ttk.Button(frame4, text="Modificar\nStock", command=root.destroy)
button5.grid(row=0, column=0, ipady=6, ipadx=10)

frame4.pack(side="top", expand=True, fill='x')

# Boton Cerrar Sesión
frame5 = tk.Frame(root)

frame5.columnconfigure((0,1), weight=1, uniform='a')

button6 = ttk.Button(frame5, text="Cerrar Sesión", command=root.destroy)
button6.grid(row=0, column=1, ipady=6, ipadx=10)

frame5.pack(side="top", expand=True, fill='x')

root.mainloop()