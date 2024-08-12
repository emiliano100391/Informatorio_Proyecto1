import tkinter as tk
from tkinter import Button, Frame,Label
from datetime import *
import MenuDesplegable as MD
#import Persona as Persona
#import Alumnos as Alumnos
#import Docentes as Docentes

app = tk.Tk()

app.configure(width=800, height=500, bg='white')
app.title('Registro Escolar')
MD.MenuD(app)

principal = Frame(app, height=300)
titulo = Label(principal, text='Registro Escolar', font=('Impact',20),fg='black').pack()
principal.pack(fill='x')
app.mainloop()