import tkinter as tk
def MenuD(self,*args):
    barra_menu = tk.Menu(self)
    self.config(menu=barra_menu)

    alumno = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Alumno', menu=alumno)

    docente = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Docente', menu=docente)

    materia= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Materia', menu=materia)


    menu_salir = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Salir', menu=menu_salir)


    menu_salir.add_command(label='Salir', command=self.quit)
