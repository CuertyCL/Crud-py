import tkinter as tk
from tkinter import ttk

# Función que se ejecuta cuando se selecciona un elemento del ComboBox
def on_select(event):
    selected_item = combo.get()
    label.config(text=f"Seleccionaste: {selected_item}")

# Crear la ventana principal
root = tk.Tk()
root.title("ComboBox Ejemplo")

# Crear un ComboBox
combo = ttk.Combobox(root, values=["Opción 1", "Opción 2", "Opción 3", "Opción 4"])
combo.pack(pady=10)

# Configurar el evento de selección
combo.bind("<<ComboboxSelected>>", on_select)

# Crear una etiqueta para mostrar la selección
label = tk.Label(root, text="Selecciona una opción")
label.pack(pady=10)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
