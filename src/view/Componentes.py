import tkinter as tk
import tkinter.ttk as ttk

class Componente(tk.Frame):
    def __init__(self):
        super().__init__()

    def add_formulario(self, titulo, isPasswd=False, ipadx=25):
        label = tk.Label(self, text=titulo, font="Impact 11")
        if not isPasswd:
            self.entry = ttk.Entry(self)
        else:
            self.entry = ttk.Entry(self, show='*')
        label.grid(row=0, column=0, sticky="w")
        self.entry.grid(row=1, column=0, ipadx=ipadx)

        self.pack(side="top", expand=True)

    def add_lista(self, titulo):
        label = tk.Label(self, text=titulo, font="Impact 11")
        combobox = ttk.Combobox(self, textvariable=None)
        label.grid(row=0, column=0, sticky="w")
        combobox.grid(row=1, column=0, ipadx=16, padx=1)

        self.pack(side="top", expand=True)

    def add_doble_boton(self, text1=None, text2=None, comm1=None, comm2=None):
        frame = tk.Frame(self)
        b1 = ttk.Button(frame, text=text1, command=comm1)
        b2 = ttk.Button(frame, text=text2, command=comm2)

        b1.pack(side="left", expand=True, ipady=6, ipadx=10, padx=20, pady=10)
        b2.pack(side="left", expand=True, ipady=6, ipadx=10, padx=20, pady=10)

        frame.pack(side="top", expand=True)

    def add_triple_boton(self, text1=None, text2=None, text3=None, comm1=None, comm2=None,  comm3=None):
        frame = tk.Frame(self)
        b1 = ttk.Button(frame, text=text1, command=comm1)
        b2 = ttk.Button(frame, text=text2, command=comm2)
        b3 = ttk.Button(frame, text=text3, command=comm3)

        b1.pack(side="left", expand=True, ipady=6, ipadx=10, padx=20, pady=10)
        b2.pack(side="left", expand=True, ipady=6, ipadx=10, padx=20, pady=10)
        b3.pack(side="left", expand=True, ipady=6, ipadx=10, padx=20, pady=10)

        frame.pack(side="top", expand=True)
    
    