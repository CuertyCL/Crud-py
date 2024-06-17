import tkinter as tk
from tkinter import messagebox

def abrir_otra_ventana():
    otra_ventana = tk.Toplevel(root)
    otra_ventana.title("Otra Ventana")
    label = tk.Label(otra_ventana, text="Esta es otra ventana")
    label.pack(padx=20, pady=20)

def on_closing():
    respuesta = messagebox.askokcancel("Salir", "¿Seguro que quieres salir?")
    if not respuesta:
        abrir_otra_ventana()  # Abrir otra ventana antes de cerrar
        root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Principal")

# Configurar la acción al cerrar la ventana
root.protocol("WM_DELETE_WINDOW", on_closing)

# Contenido de la ventana principal
label = tk.Label(root, text="Presiona la 'X' para cerrar la ventana principal")
label.pack(padx=20, pady=20)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
