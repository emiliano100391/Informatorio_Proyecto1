import tkinter as TK
from tkinter import ttk, Button, Frame,Label

docentes=[]

class Docente(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Llama al constructor de ttk.Frame
        self.nombre_label = ttk.Label(text='Nombre')
        self.nombre_entry = ttk.Entry(self)
        self.nombre_label.pack()
        self.nombre_entry.pack()
        self.apellido_label = ttk.Label(text='Apellido')
        self.apellido_entry = ttk.Entry(self)
        self.apellido_label.pack()
        self.apellido_entry.pack()
        self.aniadir = ttk.Button(text='Añadir', command=self.aniadir_docente)
        self.aniadir.pack()

        self.tabla_docente = ttk.Treeview(self, columns=('Nombre', 'Apellido'), show='headings')
        self.tabla_docente.heading('Nombre', text='Nombre')
        self.tabla_docente.heading('Apellido', text='Apellido')
        self.tabla_docente.pack(side='top')

    def aniadir_docente(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        docentes.append((nombre, apellido))
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for row in self.tabla_docente.get_children():
            self.tabla_docente.delete(row)
        for docente in docentes:
            self.tabla_docente.insert("", "end", values=docente)