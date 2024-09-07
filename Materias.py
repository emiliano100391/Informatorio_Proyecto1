from datetime import *
from tkinter import ttk,Label,Frame, Button

class Materia(ttk.Frame):
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
        self.aniadir = ttk.Button(text='Añadir', command=self.aniadir_materia)
        self.aniadir.pack()

        self.tabla_materia = ttk.Treeview(self, columns=('Nombre', 'Apellido'), show='headings')
        self.tabla_materia.heading('Nombre', text='Nombre')
        self.tabla_materia.heading('Apellido', text='Apellido')
        self.tabla_materia.pack(side='top')

    def aniadir_materia(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        materias.append((nombre, apellido))
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for row in self.tabla_materia.get_children():
            self.tabla_materia.delete(row)
        for materia in materias:
            self.tabla_materia.insert("", "end", values=materia)

materias=[]