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

principal = Frame(app,bg='white',height=500,width=500)
label_titulo = Label(principal,text='Registro Escolar',bg='white',font=('Impact',18),pady=30)
principal.pack()
label_titulo.pack()

app.mainloop()