import tkinter as tk
import tkinter.ttk as ttk
import model.Consultas as con

class Tabla():
    def create_tabla(frame, head, data):
        style = ttk.Style()
        style.configure("Custom.Treeview", 
                        background="white", 
                        foreground="black", 
                        rowheight=25, 
                        fieldbackground="white", 
                        bordercolor="black", 
                        lightcolor="black", 
                        darkcolor="black")

        style.layout("Custom.Treeview", [('Treeview.field', {'sticky': 'nswe'})])

        table = ttk.Treeview(frame, columns=head, show='headings', style="Custom.Treeview")
                
        # Encabezados
        for i in range(0, len(head)):
            table.column(head[i], anchor='center')
            table.heading(head[i], text=head[i])

        # Datos
        for j in range(0, len(data)):
            table.insert(parent='', index=tk.END, values=data[j])

        # Bordes
        for i, row in enumerate(table.get_children()):
            if i % 2 == 0:
                table.tag_configure('evenrow', background='#d3d3d3')
                table.item(row, tags=('evenrow',))
            else:
                table.tag_configure('oddrow', background='#ffffff')
                table.item(row, tags=('oddrow',))
            

        # Scrollbar
        scrollbarv = tk.Scrollbar(frame, orient='vertical', command=table.yview)
        scrollbarv.place(relx=1, rely=0, relheight=1, anchor='ne')
        table.configure(yscrollcommand=scrollbarv.set)

        scrollbarh = tk.Scrollbar(frame, orient='horizontal', command=table.xview)
        scrollbarh.place(relx=0, rely=1, relwidth=1, anchor='sw')
        table.configure(xscrollcommand=scrollbarh.set)

        table.pack(expand=True, fill='both')
