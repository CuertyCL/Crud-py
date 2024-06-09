import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

ancho = 1024
alto = 768
x = (root.winfo_screenwidth()//2)-(ancho//2)
y = (root.winfo_screenheight()//2)-(alto//2)
root.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))

root.title("Inventario")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

root.rowconfigure((0, 2), weight=1)
root.rowconfigure(1, weight=4)

# Logo y titulo

image = tk.PhotoImage(file="./logo_128x128.png")
labelimg = tk.Label(root, image=image)
label = tk.Label(root, text="INVENTARIO", font=("Impact", 24))

labelimg.grid(row=0, column=0, sticky="nw")
label.grid(row=0, column=0, sticky="ne", pady=50)


# Lista de productos
lista = ["Columna 1", "Columna 2", "Columna 3", "Columna 4", "Columna 5"]

combo = ttk.Combobox(root, values=lista)

combo.grid(row=0, column=1)

# Botones de filtrado
fbotones = tk.Frame(root, highlightbackground="gray", highlightthickness=4)
fbotones.grid(row=1, column=0, sticky="nsew", padx=15, pady=15)

b1 = ttk.Button(fbotones, text="Filtrar")
b1.pack(side="top", expand=True, ipady=6, ipadx=10)

b2 = ttk.Button(fbotones, text="Generar\nLista")
b2.pack(side="top", expand=True, ipady=6, ipadx=10)


# Tabla
ftabla = tk.Frame(root)
ftabla.grid(row=1, column=1, sticky="nsew", padx=15)

label = tk.Label(ftabla, bg="red")
label.pack(expand=True, fill="both")

# Boton Salir
bsalir = ttk.Button(root, text="Volver", command=root.destroy)
bsalir.grid(row=2, column=0, ipady=6, ipadx=10)


root.mainloop()
