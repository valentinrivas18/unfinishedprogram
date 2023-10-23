import tkinter as tk
from tkinter import ttk
from tkinter import Menu

# inicializando la ventana
# con el nombre de arriba
ventana = tk.Tk()
ventana.title("IMC -- QDD PROGRAM")

# con esta linea establesco el temaño de la ventana
# y con la otra lo que hago es que la ventana no se pueda
# redimensionar es decir cambiar de tamaño
ventana.geometry("300x150+900+300")
ventana.resizable(0,0)

#voy a gregar une etiqueta indicando el numero de estudiantes
etiqueta1 = ttk.Label(ventana, text="N° Estudiantes")
etiqueta1.grid(column=0, row=0)

## la funcion que desactiva toda vaina

# agregare un boton con las siguientes lineas de codigo
# se crea la funcion que seraw la responsable de accionar las acciones
# al presionar el boton

def funcion_click():
    aceptar.configure(text="Aceptar")
    etiqueta1.configure(foreground='blue')
    aceptar.configure(state="disabled")
    preguntar_nostud.configure(state="disabled")

# aqui creamos el boton como un objeto
aceptar = ttk.Button(ventana, text="Aceptar", command=funcion_click)
aceptar.grid(column=0, row=2)

# esta seria la caja de texto
nostud = tk.IntVar()
preguntar_nostud = ttk.Entry(ventana, width=20, textvariable=nostud)
preguntar_nostud.grid(column=1, row=0)

#voy a gregar une etiqueta indicando el nombre del estudiante
etiqueta2= ttk.Label(ventana, text="Nombre del Estudiante")
etiqueta2.grid(column=0, row=3)

# esta seria la caja de texto
nomstud = tk.StringVar()
preguntar_nomstud = ttk.Entry(ventana, width=20, textvariable=nomstud)
preguntar_nomstud.grid(column=1, row=3)

# #voy a gregar une etiqueta indicando Estatura del Estudiante
etiqueta3= ttk.Label(ventana, text="Estatura del Estudiante")
etiqueta3.grid(column=0, row=4)

# # esta seria la caja de texto
estud = tk.StringVar()
preguntar_estud = ttk.Entry(ventana, width=20, textvariable=estud)
preguntar_estud.grid(column=1, row=4)

# #voy a gregar une etiqueta indicando el Peso del Estudiante
etiqueta4= ttk.Label(ventana, text="Peso del Estudiante")
etiqueta4.grid(column=0, row=5)

# # esta seria la caja de texto
pestud = tk.StringVar()
preguntar_pestud = ttk.Entry(ventana, width=20, textvariable=pestud)
preguntar_pestud.grid(column=1, row=5)

# agregare un boton con las siguientes lineas de codigo
# se crea la funcion que seraw la responsable de accionar las acciones
# al presionar el boton

def funcion_click1():
    Agregar.configure(text="Agregar")


# aqui creamos el boton como un objeto
Agregar = ttk.Button(ventana, text="Agregar", command=funcion_click1)
Agregar.grid(column=0, row=6)

# guardar por fin el pdf

def guardar_1():
    Guardar.configure(text="Agregar")


# aqui creamos el boton como un objeto
Guardar = ttk.Button(ventana, text="Guardar", command=funcion_click1)
Guardar.grid(column=1, row=6)

#AQUI VAMOS A DESACTIVAR TODOS LOS TEXT BOX HASTA QUE NO SE LE DE CLICK
#A "ACEPTAR"



# esta linea es para que la ventana nunca se cierre

ventana.mainloop()