import tkinter as tk


'''
ventana = tk.Tk()
ventana.title("Mi primer ventana")
'''

'''
Orden para el control de la ventana en los taños y posiciones
#ventana.geometry("<ancho>x<alto>+<posición_x>+<posición_y>")
#ventana.geometry("500x500+500+200")
'''

'''
# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Calcular las coordenadas para centrar la ventana
ancho_ventana = 800
alto_ventana = 600
posicion_x = (ancho_pantalla - ancho_ventana) // 2
posicion_y = (alto_pantalla - alto_ventana) // 2

# Establecer el tamaño y la posición de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
'''

'''
text: Establece el texto que se muestra en la etiqueta.
font: Define la fuente y el tamaño del texto en la etiqueta.
bg o background: Establece el color de fondo de la etiqueta.
fg o foreground: Define el color del texto en la etiqueta.
width: Especifica el ancho de la etiqueta en caracteres.
height: Define la altura de la etiqueta en líneas.
anchor: Controla la alineación del texto dentro de la etiqueta.
image: Especifica la imagen que se mostrará en la etiqueta. Puedes proporcionar una instancia de PhotoImage o ImageTk.PhotoImage como valor para este parámetro.



etiqueta = tk.Label(ventana, text="¡Hola, mundo!", bg="yellow", fg="red", font=("Arial", 50), width=20, height=2, anchor="nw")
etiqueta.pack()

config sirve para actualizar cualquier valor los anteriores
etiqueta.config(text="Nuevo texto")
'''

'''
def cambiar_texto():
    etiqueta.config(text="¡Texto cambiado!")

ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Texto original")
etiqueta.pack()
# Crear un botón con texto y función de comando
boton1 = tk.Button(ventana, text="Cambiar", command=cambiar_texto)
boton1.pack()

# Crear un botón con colores de fondo y texto personalizados
boton2 = tk.Button(ventana, text="Botón 2", bg="blue", fg="white", font=("Arial", 12))
boton2.pack()

# Crear un botón deshabilitado
boton3 = tk.Button(ventana, text="Deshabilitado", state="disabled")
boton3.pack()

# Obtener las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth() #método para obtener Ancho
alto_pantalla = ventana.winfo_screenheight() #método para obtener Alto

# Calcular las coordenadas para centrar la ventana
ancho_ventana = 400
alto_ventana = 200
posicion_x = (ancho_pantalla - ancho_ventana) // 2
posicion_y = (alto_pantalla - alto_ventana) // 2

# Establecer el tamaño y la posición de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")
'''

'''
def obtener_texto():
    texto_ingresado = cuadro_texto.get()
    etiqueta.config(text="Texto ingresado: " + texto_ingresado)

ventana = tk.Tk()

etiqueta = tk.Label(ventana, text="Texto ingresado: ")
etiqueta.pack()

cuadro_texto = tk.Entry(ventana, width=30)
cuadro_texto.pack()

boton = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton.pack()
'''

'''
ventana = tk.Tk()
# Crear un marco con borde sólido
marco1 = tk.Frame(ventana, width=200, height=100, bd=2, relief="solid")
marco1.pack()

# Agregar una etiqueta al marco1
etiqueta1 = tk.Label(marco1, text="Marco 1")
etiqueta1.pack()
etiqueta3 = tk.Label(marco1, text="Marco 1")
etiqueta3.pack()
# Crear un marco con borde en relieve
marco2 = tk.Frame(ventana, width=200, height=100, bd=2, relief="raised")
marco2.pack()

# Agregar una etiqueta al marco2
etiqueta2 = tk.Label(marco2, text="Marco 2")
etiqueta2.pack()
'''

def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        print("Elemento seleccionado:", elemento)

ventana = tk.Tk()

cuadro_lista = tk.Listbox(ventana, width=30, selectmode="multiple")
cuadro_lista.pack()

elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]

for elemento in elementos:
    cuadro_lista.insert(tk.END, elemento)

boton = tk.Button(ventana, text="Obtener", command=obtener_seleccion)
boton.pack()

ventana.mainloop()