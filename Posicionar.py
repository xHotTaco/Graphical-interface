import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x200")

label = tk.Label(ventana, text="Ejemplo")
label.place(x=50, y=50)

ventana.mainloop()