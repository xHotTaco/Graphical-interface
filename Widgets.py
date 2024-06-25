#Para esto tenemos las siguientes herramientas

#Label (etiqueta)

import tkinter as tk

ventana = tk.Tk()

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Calcular las coordenadas para centrar la ventana
ancho_ventana = 300
alto_ventana = 100
posicion_x = (ancho_pantalla - ancho_ventana) // 2
posicion_y = (alto_pantalla - alto_ventana) // 2

# Establecer el tamaño y la posición de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

'''
Tambien se le puede agregar o editar el componente 
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")

text: Establece el texto que se muestra en la etiqueta.
font: Define la fuente y el tamaño del texto en la etiqueta.
bg o background: Establece el color de fondo de la etiqueta.
fg o foreground: Define el color del texto en la etiqueta.
width: Especifica el ancho de la etiqueta en caracteres.
height: Define la altura de la etiqueta en líneas.
anchor: Controla la alineación del texto dentro de la etiqueta.
image: Especifica la imagen que se mostrará en la etiqueta. Puedes proporcionar una instancia de PhotoImage o ImageTk.PhotoImage como valor para este parámetro.
'''
#etiqueta = tk.Label(ventana, text="¡Hola, mundo!", bg="yellow", fg="blue", font=("Arial", 16), width=20, height=2, anchor="center")

'''
Se utiliza el .pack() Para poder hacer visible la etiqueta en la ventana 
'''
#etiqueta.pack()

#Metodo Config
'''
Se utiliza para poder configurar un parametro en especifico para poder despues
modificarlo
'''

etiqueta = tk.Label(ventana, text="Texto inicial")
etiqueta.pack()

# Actualizar el texto de la etiqueta
etiqueta.config(text="Nuevo texto")

'''
El método config se puede utilizar para cambiar varias opciones del widget Label, como:

text: Permite establecer o cambiar el texto mostrado en la etiqueta.
font: Permite cambiar la fuente y el tamaño del texto en la etiqueta.
bg o background: Permite cambiar el color de fondo de la etiqueta.
fg o foreground: Permite cambiar el color del texto en la etiqueta.
width: Permite cambiar el ancho de la etiqueta en caracteres.
height: Permite cambiar la altura de la etiqueta en líneas.
anchor: Permite cambiar la alineación del texto dentro de la etiqueta.
Puedes utilizar el método config con cualquier opción válida para el widget Label y asignarle un nuevo valor para actualizarla.
'''


ventana.mainloop()