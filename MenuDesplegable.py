import tkinter as tk

ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('400x200') 

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu)
barra_menu.add_cascade(label = 'Principal', menu=menu_principal)

submenu = tk.Menu(menu_principal)
menu_principal.add_cascade(label = 'Opciones', menu=submenu)

submenu.add_command(label = 'Opción 1')
submenu.add_command(label = 'Opción 2')

ventana.mainloop()


#TEXTO DE PRUEBA SOY PABLO
#CAMBIOS EN EL MENU PDF Y AGREGUE AL BOTON EDICION TRES OPCIONES
import tkinter as tk

ventana = tk.Tk()
ventana.title('EQUIPO 2 - Menú desplegable')
ventana.geometry('600x400') 


barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Archivo', menu=menu_archivo)


menu_archivo.add_command(label='Nuevo Archivo')
menu_archivo.add_command(label='Abrir')
menu_archivo.add_separator()
menu_archivo.add_command(label='Guardar')
menu_archivo.add_command(label='Guardar Como...')
menu_archivo.add_separator()
menu_archivo.add_command(label='Convertir a PDF')

menu_edicion = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Edición', menu=menu_edicion)

menu_edicion.add_command(label = 'Copiar')
menu_edicion.add_command(label = 'Cortar')
menu_edicion.add_command(label = 'Pegar')


menu_acerca = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Acerca de', menu=menu_acerca)


menu_salir = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Salir', menu=menu_salir)


menu_salir.add_command(label='Salir', command=ventana.quit)


ventana.mainloop()
