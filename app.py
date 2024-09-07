import tkinter as tk
from tkinter import *
from tkinter import Button, Frame, Label, ttk
import Alumnos as Alumnos
import Docentes as Docentes
import Materias as Materias

class App(ttk.Frame):
    def __init__(self, main_windows):
        super().__init__(main_windows)
        main_windows.title("Registro Escolar")
        self.notebook = ttk.Notebook(self)

        # Crear las secciones Alumno, Docente y Materia
        self.alumno = Alumnos.Alumno(self.notebook)
        self.notebook.add(self.alumno, text='Alumno')

        self.docente = Docentes.Docente(self.notebook)
        self.notebook.add(self.docente, text='Docentes')

        self.materia = Materias.Materia(self.notebook)
        self.notebook.add(self.materia, text='Materia')

        self.notebook.pack(padx=10, pady=10)
        self.pack()
        
main_windows= tk.Tk()
app = App(main_windows)

barra_menu = tk.Menu(main_windows)
main_windows.config(menu=barra_menu)
menu_salir = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Salir', menu=menu_salir)
menu_salir.add_command(label='Salir', command=main_windows.quit)

app.mainloop()