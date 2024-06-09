import vista.Elementos as elem

root = elem.Ventana()
root.menu("Inicio")

comp1 = elem.Contenedor(root)
comp1.addTitulo("INICIO", "logo_sin_fondo_v2_128x128.png")
comp1.addFrame()

# Botones Dobles
b1 = elem.Contenedor(root)
b1.addDobleBoton("Modificar\n Stock", "Modificar\n Inventario")
b1.addFrame(after=comp1, pady=15)

b2 = elem.Contenedor(root)
b2.addDobleBoton("Añadir\n Venta", "Modificar\n Menu")
b2.addFrame(after=b1, pady=15)

root.mainloop()

