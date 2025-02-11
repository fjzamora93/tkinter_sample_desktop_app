import tkinter as tk
from tkinter import ttk
from tkinter import *
from database.dbconnection import insertar_datos
from ventana_fichero import *
from util.to_json import guardar_datos_json
from ventana_fichero import *
import controller.controller_empleado as controller

def altas():

    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Formulario de alta")
    ventana.geometry("1200x600")

    # Crear un marco para contener el contenido
    marco = tk.Frame(ventana)
    marco.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    # Configurar las columnas para que se expandan y se centren
    ventana.grid_columnconfigure(0, weight=1)  
    marco.grid_columnconfigure(0, weight=1)
    marco.grid_columnconfigure(1, weight=1)
    marco.grid_columnconfigure(2, weight=1)
    marco.grid_columnconfigure(3, weight=1)
    marco.grid_columnconfigure(4, weight=1)
    marco.grid_columnconfigure(5, weight=1)

    # PRIMERA FILA: Apellido y Nombre
    label_nombre = tk.Label(marco, text="Apellido y Nombre")
    label_nombre.grid(row=0, column=0, padx=10, pady=5, sticky="ew", columnspan=6)
    global entry_nombre
    entry_nombre = tk.Entry(marco)
    entry_nombre.grid(row=1, column=0, padx=10, pady=5, sticky="ew", columnspan=6)
 

    # SEGUNDA FILA: Fecha de Inicio, Fecha de Nacimiento, Dirección
    # Columna 0
    label_fecha_inicio = tk.Label(marco, text="Fecha de Inicio")
    label_fecha_inicio.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
    global entry_fecha_inicio
    entry_fecha_inicio = tk.Entry(marco)
    entry_fecha_inicio.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

    # Columna 1
    label_fecha_nacimiento = tk.Label(marco, text="Fecha de Nacimiento")
    label_fecha_nacimiento.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
    global entry_fecha_nacimiento
    entry_fecha_nacimiento = tk.Entry(marco)
    entry_fecha_nacimiento.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    # Columna 2 
    label_direccion = tk.Label(marco, text="Dirección")
    label_direccion.grid(row=2, column=2, padx=10, pady=5, sticky="ew")
    global entry_direccion
    entry_direccion = tk.Entry(marco)
    entry_direccion.grid(row=3, column=2, padx=10, pady=5, sticky="ew", columnspan=4)

   # TERCERA FILA: NIF, Datos Bancarios, Afiliación SS
    # Columna 0
    label_nif = tk.Label(marco, text="NIF")
    label_nif.grid(row=4, column=0, padx=10, pady=6, sticky="ew")
    global entry_nif
    entry_nif = tk.Entry(marco)
    entry_nif.grid(row=5, column=0, padx=10, pady=6, sticky="ew")

    # Columna 1
    label_datos_bancarios = tk.Label(marco, text="Datos Bancarios")
    label_datos_bancarios.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
    global entry_datos_bancarios
    entry_datos_bancarios = tk.Entry(marco)
    entry_datos_bancarios.grid(row=5, column=1, padx=10, pady=5, sticky="ew", columnspan=3)

    # Columna 2 
    label_afiliacion = tk.Label(marco, text="Afiliación SS")
    label_afiliacion.grid(row=4, column=4, padx=10, pady=5, sticky="ew")
    global entry_afiliacion
    entry_afiliacion = tk.Entry(marco)
    entry_afiliacion.grid(row=5, column=4, padx=10, pady=5, sticky="ew", columnspan=2)

    # CUARTA FILA: Género, Departamento, Puesto
    # Columna 0
    label_genero = tk.Label(marco, text="Género")
    label_genero.grid(row=6, column=0, padx=10, pady=6, sticky="ew")
    global entry_genero
    entry_genero = tk.Entry(marco)
    entry_genero.grid(row=7, column=0, padx=10, pady=6, sticky="ew")

    # Columna 1
    label_departamento = tk.Label(marco, text="Departamento")
    label_departamento.grid(row=6, column=1, padx=10, pady=6, sticky="ew")
    global entry_departamento
    entry_departamento = tk.Entry(marco)
    entry_departamento.grid(row=7, column=1, padx=10, pady=6, sticky="ew", columnspan=3)

    # Columna 2 
    label_puesto = tk.Label(marco, text="Puesto")
    label_puesto.grid(row=6, column=4, padx=10, pady=6, sticky="ew")
    global entry_puesto
    entry_puesto = tk.Entry(marco)
    entry_puesto.grid(row=7, column=4, padx=10, pady=6, sticky="ew", columnspan=2)


    # QUINTA FILA : TEléfono, salario, IRPF
    label_telefono = tk.Label(marco, text="Teléfono")
    label_telefono.grid(row = 8, column = 0, padx=5, pady=6, sticky="ew")
    global entry_telefono
    entry_telefono = tk.Entry(marco)
    entry_telefono.grid(row = 8, column = 1, padx=10, pady=6, sticky="ew")

    label_salario = tk.Label(marco, text="Salario")
    label_salario.grid(row = 8, column = 2, padx=5, pady=6, sticky="ew")
    global entry_salario
    entry_salario = tk.Entry(marco)
    entry_salario.grid(row = 8, column = 3, padx=10, pady=6, sticky="ew")

    label_irpf = tk.Label(marco, text="IRPF")
    label_irpf.grid(row = 8, column = 4, padx=5, pady=6, sticky="ew")
    global entry_irpf
    entry_irpf = tk.Entry(marco)
    entry_irpf.grid(row = 8, column = 5, padx=10, pady=6, sticky="ew")

    # SEXTA FILA: email, pagas extras, seg. social
    label_email = tk.Label(marco, text="Email")
    label_email.grid(row = 9, column = 0, padx=5, pady=6, sticky="ew")
    global entry_email
    entry_email = tk.Entry(marco)
    entry_email.grid(row = 9, column = 1, padx=10, pady=6, sticky="ew")

    label_pagas_extras = tk.Label(marco, text="Pagas Extras")
    label_pagas_extras.grid(row = 9, column = 2, padx=5, pady=6, sticky="ew")
    global entry_pagas_extras
    entry_pagas_extras = tk.Entry(marco)
    entry_pagas_extras.grid(row = 9, column = 3, padx=10, pady=6, sticky="ew")

    label_seg_social = tk.Label(marco, text="Seguridad Social")
    label_seg_social.grid(row = 9, column = 4, padx=5, pady=6, sticky="ew")
    global entry_seg_social
    entry_seg_social = tk.Entry(marco)
    entry_seg_social.grid(row = 9, column = 5, padx=10, pady=6, sticky="ew")


    # BOTÓN INSERTAR
    boton1 = ttk.Button(marco, text="Alta empleado", command=lambda: handle_data(), style="TButton", width=60)
    boton1.grid(row = 10, column = 4, columnspan=2, padx=10, pady=10)

    # Bucle principal
    ventana.mainloop()

def handle_data():
    """"
    Esto sería mejor manenejarlo con un ViewModel o alguna especie de servicio que respondiese a los cambios en la vista... pero bueno, 
    lo convertimos en variables locales para no tener que estar mareando los parámetros de un sitio a otro y lo resolvemos todo aquí en la vista.
    """
    controller.add_employee(
        entry_nombre.get(),
        entry_seg_social.get(),
        entry_pagas_extras.get(),
        entry_email.get(),
        entry_irpf.get(),
        entry_salario.get(),
        entry_telefono.get(),
        entry_puesto.get(),
        entry_departamento.get(),
        entry_genero.get(),
        entry_afiliacion.get(),
        entry_datos_bancarios.get(),
        entry_fecha_nacimiento.get(),
        entry_nif.get(),
        entry_direccion.get(),
        entry_fecha_inicio.get()
    )
    guardar_datos_json()
    ventana_fichero()



if __name__ == "__main__":
    altas()
