import tkinter as tk

def cerrar_y_abrir():
    global root  # Utilizamos global para poder destruir la ventana principal
    
    # Destruir la ventana principal
    root.destroy()

    # Crear una nueva ventana
    nueva_ventana = tk.Tk()
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("300x200")

    # Contenido de la nueva ventana
    label = tk.Label(nueva_ventana, text="¡Nueva ventana abierta!")
    label.pack(pady=20)

    # Botón para cerrar la nueva ventana
    btn_cerrar = tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
    btn_cerrar.pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Principal")
root.geometry("300x200")

# Botón para cerrar la ventana actual y abrir una nueva
btn_abrir_nueva_ventana = tk.Button(root, text="Abrir Nueva Ventana", command=cerrar_y_abrir)
btn_abrir_nueva_ventana.pack(pady=20)

# Ejecutar el bucle principal de la ventana
root.mainloop()
