import tkinter as tk
from datetime import *
import MenuDesplegable as MD
#import Persona as Persona
#import Alumnos as Alumnos
#import Docentes as Docentes

app = tk.Tk()

app.configure(width=800, height=500, bg='white')
app.title('Registro Escolar')
MD.MenuD(app)
app.mainloop()