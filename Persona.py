import tkinter as TK
from datetime import *
class Persona:
    def __init__(self, apellido, nombre, fNacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fNacimiento = fNacimiento
    
    def Edad(self, fNacimiento):
        anio = date.today().year
        edad = anio - fNacimiento
        return edad