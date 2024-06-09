import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()
ancho = 350
alto = 430
x = (root.winfo_screenwidth()//2)-(ancho//2)
y = (root.winfo_screenheight()//2)-(alto//2)

root.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))
root.resizable(False, False)

frame1 = tk.Frame(root)

# Titulo y Logo
image =tk. PhotoImage(file="./logo_128x128.png")
labelimg = tk.Label(frame1, image=image)
label = tk.Label(frame1, text="INICIO", font=("Impact", 24))
labelimg.pack(side="left", expand=True)
label.pack(side="left", expand=True)

frame1.pack(side="top", expand=True)

# Boton
button = ttk.Button(root, text="Ver\nTablas", command=root.destroy)
button.pack(side="top", expand=True, ipady=6, ipadx=10)

# Boton
button1 = ttk.Button(root, text="Modificar\nStock", command=root.destroy)
button1.pack(side="top", expand=True, ipady=6, ipadx=10)

# Boton
button2 = ttk.Button(root, text="Añadir\nVenta", command=root.destroy)
button2.pack(side="top", expand=True, ipady=6, ipadx=10)

# Boton
frame2 = tk.Frame(root)

button3 = ttk.Button(root, text="Cerrar Sesión", command=root.destroy)
button3.pack(side="right", padx=50, pady=25, ipady=6, ipadx=10)
frame2.pack(side="top", expand=True)


root.mainloop()