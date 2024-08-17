import tkinter as tk
def MenuD(app):
    barra_menu = tk.Menu(app)
    app.config(menu=barra_menu)

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


    menu_salir.add_command(label='Salir', command=app.quit)
