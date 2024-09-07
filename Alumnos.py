import tkinter as TK
from tkinter import Label, ttk, Frame

alumnos=[]
class Alumno(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.nombre_label = ttk.Label(text='Nombre')
        self.nombre_entry = ttk.Entry(self)
        self.nombre_label.pack()
        self.nombre_entry.pack()

        self.apellido_label = ttk.Label(text='Apellido')
        self.apellido_entry = ttk.Entry(self)
        self.apellido_label.pack()
        self.apellido_entry.pack()

        self.aniadir = ttk.Button(text='Añadir', command=self.aniadir_alumno)
        self.aniadir.pack()

        # Crear la tabla de alumnos
        self.tabla_alumno = ttk.Treeview(self, columns=('Nombre', 'Apellido'), show='headings')
        self.tabla_alumno.heading('Nombre', text='Nombre')
        self.tabla_alumno.heading('Apellido', text='Apellido')
        self.tabla_alumno.pack(side='top')

    def aniadir_alumno(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        alumnos.append((nombre, apellido))
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for row in self.tabla_alumno.get_children():
            self.tabla_alumno.delete(row)
        for alumno in alumnos:
            self.tabla_alumno.insert("", "end", values=alumno)
