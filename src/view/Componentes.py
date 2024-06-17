import tkinter as tk
import tkinter.ttk as ttk

class Componente(tk.Frame):
    def __init__(self, root=None, heigth=None, width=None):
        if heigth is None and width is None:
            super().__init__(root)
        elif heigth is None and width is not None:
            super().__init__(root,  width=width)
        elif heigth is not None and width is None:
            super().__init__(root,  height=heigth)
        else:
            super().__init__(root, height=heigth, width=width)

    def add_formulario(self, titulo, isPasswd=False, ipadx=25, side='top'):
        label = tk.Label(self, text=titulo, font="Impact 11")
        if not isPasswd:
            self.entry = ttk.Entry(self)
        else:
            self.entry = ttk.Entry(self, show='*')
        label.grid(row=0, column=0, sticky="w")
        self.entry.grid(row=1, column=0, ipadx=ipadx)

        self.pack(side=side, expand=True)

    def get_entry(self):
        return self.entry.get()

    def add_lista(self, titulo, side='top', values=[], default="-- Selecciona uno --"):
        self.label = tk.Label(self, text=titulo, font="Impact 11")
        values.insert(0, default)
        self.combobox = ttk.Combobox(self, textvariable=None)
        self.combobox["values"] = values
        self.combobox.current(0)
        self.label.grid(row=0, column=0, sticky="w")
        self.combobox.grid(row=1, column=0, ipadx=16, padx=1)

        self.pack(side=side, expand=True)

    def get_selected_list(self):
        return self.combobox.get()

    def add_doble_boton(self, text1=None, text2=None, comm1=None, comm2=None, ipady=6, ipadx=10, padx=20, pady=10, side='top'):
        frame = tk.Frame(self)
        b1 = ttk.Button(frame, text=text1, command=comm1)
        b2 = ttk.Button(frame, text=text2, command=comm2)

        b1.pack(side="left", expand=True, ipady=ipady, ipadx=ipadx, padx=padx, pady=pady)
        b2.pack(side="left", expand=True, ipady=ipady, ipadx=ipadx, padx=padx, pady=pady)

        frame.pack(side=side, expand=True)

    def add_triple_boton(self, text1=None, text2=None, text3=None, comm1=None, comm2=None,  comm3=None, side='top', ipady=6, ipadx=10, padx=20, pady=10):
        frame = tk.Frame(self)
        b1 = ttk.Button(frame, text=text1, command=comm1)
        b2 = ttk.Button(frame, text=text2, command=comm2)
        b3 = ttk.Button(frame, text=text3, command=comm3)

        b1.pack(side="left", expand=True, ipady=ipady, ipadx=ipadx, padx=padx, pady=pady)
        b2.pack(side="left", expand=True, ipady=ipady, ipadx=ipadx, padx=padx, pady=pady)
        b3.pack(side="left", expand=True, ipady=ipady, ipadx=ipadx, padx=padx, pady=pady)

        frame.pack(side=side, expand=True)
    
    def create_table(self, head, data, side='top'):
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

        table = ttk.Treeview(self, columns=head, show='headings',style="Custom.Treeview")
                
        # Encabezados
        for i in range(0, len(head)):
            table.column(head[i], anchor='center', width=80)
            table.heading(head[i], text=head[i], anchor='center')

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
        scrollbarv = tk.Scrollbar(self, orient='vertical', command=table.yview)
        scrollbarv.place(relx=1, rely=0, relheight=1, anchor='ne')
        table.configure(yscrollcommand=scrollbarv.set)

        scrollbarh = tk.Scrollbar(self, orient='horizontal', command=table.xview)
        scrollbarh.place(relx=0, rely=1, relwidth=1, anchor='sw')
        table.configure(xscrollcommand=scrollbarh.set)

        table.pack(side=side, expand=True, fill='both')
    