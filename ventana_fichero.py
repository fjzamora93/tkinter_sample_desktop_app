import tkinter as tk
from tkinter import ttk
from tkinter import *
import controller.controller_empleado as controller
from models.EmpleadoDTO import EmpleadoDTO

def ventana_fichero():

    # Crear ventana
    ventana = tk.Tk()
    ventana.title("Fichero del empleado")
    ventana.geometry("1200x600")

    # Crear un marco para contener el contenido
    marco = tk.Frame(ventana)
    marco.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    empleado: EmpleadoDTO = controller.obtener_empleado()

    # Configurar las columnas para que se expandan y se centren
    ventana.grid_columnconfigure(0, weight=1)  
    marco.grid_columnconfigure(0, weight=1)
    marco.grid_columnconfigure(1, weight=1)
    marco.grid_columnconfigure(2, weight=1)
    marco.grid_columnconfigure(3, weight=1)
    marco.grid_columnconfigure(4, weight=1)
    marco.grid_columnconfigure(5, weight=1)

    # PRIMERA FILA: Apellido y Nombre
    label_nombre_text = tk.Label(marco, text="Nombre:", font=("Arial", 10, "bold"))
    label_nombre_text.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
    label_nombre = tk.Label(marco, text=empleado.nombre)
    label_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="ew", columnspan=5)

    # SEGUNDA FILA: Fecha de Inicio, Fecha de Nacimiento, Dirección
    # Columna 0
    label_fecha_inicio_text = tk.Label(marco, text="Fecha de Inicio:", font=("Arial", 10, "bold"))
    label_fecha_inicio_text.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
    label_fecha_inicio = tk.Label(marco, text=empleado.fecha_inicio)
    label_fecha_inicio.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    # Columna 1
    label_fecha_nacimiento_text = tk.Label(marco, text="Fecha de Nacimiento:", font=("Arial", 10, "bold"))
    label_fecha_nacimiento_text.grid(row=2, column=2, padx=10, pady=5, sticky="ew")
    label_fecha_nacimiento = tk.Label(marco, text=empleado.fecha_nacimiento)
    label_fecha_nacimiento.grid(row=2, column=3, padx=10, pady=5, sticky="ew")

    # Columna 2 
    label_direccion_text = tk.Label(marco, text="Dirección:", font=("Arial", 10, "bold"))
    label_direccion_text.grid(row=2, column=4, padx=10, pady=5, sticky="ew")
    label_direccion = tk.Label(marco, text=empleado.direccion)
    label_direccion.grid(row=2, column=5, padx=10, pady=5, sticky="ew")

    separador_horizontal = ttk.Separator(marco, orient="horizontal")
    separador_horizontal.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

    # TERCERA FILA: NIF, Datos Bancarios, Afiliación SS
    # Columna 0
    label_nif_text = tk.Label(marco, text="NIF:", font=("Arial", 10, "bold"))
    label_nif_text.grid(row=4, column=0, padx=10, pady=6, sticky="ew")
    label_nif = tk.Label(marco, text=empleado.nif)
    label_nif.grid(row=4, column=1, padx=10, pady=6, sticky="ew")

    # Columna 1
    label_datos_bancarios_text = tk.Label(marco, text="Datos Bancarios:", font=("Arial", 10, "bold"))
    label_datos_bancarios_text.grid(row=4, column=2, padx=10, pady=5, sticky="ew")
    label_datos_bancarios = tk.Label(marco, text=empleado.datos_bancarios)
    label_datos_bancarios.grid(row=4, column=3, padx=10, pady=5, sticky="ew")

    # Columna 2 
    label_afiliacion_text = tk.Label(marco, text="Afiliación SS:", font=("Arial", 10, "bold"))
    label_afiliacion_text.grid(row=4, column=4, padx=10, pady=5, sticky="ew")
    label_afiliacion = tk.Label(marco, text=empleado.afiliacion)
    label_afiliacion.grid(row=4, column=5, padx=10, pady=5, sticky="ew")

    # CUARTA FILA: Género, Departamento, Puesto
    # Columna 0
    label_genero_text = tk.Label(marco, text="Género:", font=("Arial", 10, "bold"))
    label_genero_text.grid(row=6, column=0, padx=10, pady=6, sticky="ew")
    label_genero = tk.Label(marco, text=empleado.genero)
    label_genero.grid(row=6, column=1, padx=10, pady=6, sticky="ew")

    # Columna 1
    label_departamento_text = tk.Label(marco, text="Departamento:", font=("Arial", 10, "bold"))
    label_departamento_text.grid(row=6, column=2, padx=10, pady=6, sticky="ew")
    label_departamento = tk.Label(marco, text=empleado.departamento)
    label_departamento.grid(row=6, column=3, padx=10, pady=6, sticky="ew")

    # Columna 2 
    label_puesto_text = tk.Label(marco, text="Puesto:", font=("Arial", 10, "bold"))
    label_puesto_text.grid(row=6, column=4, padx=10, pady=6, sticky="ew")
    label_puesto = tk.Label(marco, text=empleado.puesto)
    label_puesto.grid(row=6, column=5, padx=10, pady=6, sticky="ew")

    # QUINTA FILA : Teléfono, salario, IRPF
    label_telefono_text = tk.Label(marco, text="Teléfono:", font=("Arial", 10, "bold"))
    label_telefono_text.grid(row=8, column=0, padx=5, pady=6, sticky="ew")
    label_telefono = tk.Label(marco, text=empleado.telefono)
    label_telefono.grid(row=8, column=1, padx=5, pady=6, sticky="ew")

    label_salario_text = tk.Label(marco, text="Salario:", font=("Arial", 10, "bold"))
    label_salario_text.grid(row=8, column=2, padx=5, pady=6, sticky="ew")
    label_salario = tk.Label(marco, text=empleado.salario)
    label_salario.grid(row=8, column=3, padx=5, pady=6, sticky="ew")

    label_irpf_text = tk.Label(marco, text="IRPF:", font=("Arial", 10, "bold"))
    label_irpf_text.grid(row=8, column=4, padx=5, pady=6, sticky="ew")
    label_irpf = tk.Label(marco, text=empleado.irpf)
    label_irpf.grid(row=8, column=5, padx=5, pady=6, sticky="ew")

    # SEXTA FILA: email, pagas extras, seg. social
    label_email_text = tk.Label(marco, text="Email:", font=("Arial", 10, "bold"))
    label_email_text.grid(row=9, column=0, padx=5, pady=6, sticky="ew")
    label_email = tk.Label(marco, text=empleado.email)
    label_email.grid(row=9, column=1, padx=5, pady=6, sticky="ew")

    label_pagas_extras_text = tk.Label(marco, text="Pagas Extras:", font=("Arial", 10, "bold"))
    label_pagas_extras_text.grid(row=9, column=2, padx=5, pady=6, sticky="ew")
    label_pagas_extras = tk.Label(marco, text=empleado.pagas_extras)
    label_pagas_extras.grid(row=9, column=3, padx=5, pady=6, sticky="ew")

    label_seg_social_text = tk.Label(marco, text="Seguridad Social:", font=("Arial", 10, "bold"))
    label_seg_social_text.grid(row=9, column=4, padx=5, pady=6, sticky="ew")
    label_seg_social = tk.Label(marco, text=empleado.seg_social)
    label_seg_social.grid(row=9, column=5, padx=5, pady=6, sticky="ew")

    separador_horizontal = ttk.Separator(marco, orient="horizontal")
    separador_horizontal.grid(row=10, column=0, columnspan=2, sticky="ew", pady=10)

    # BOTÓN OTRO EMPLEADO
    boton1 = ttk.Button(marco, text="Cerrar", command=ventana.destroy, style="TButton", width=60)
    boton1.grid(row=10, column=4, columnspan=2, padx=10, pady=10)

    # Bucle principal
    ventana.mainloop()

if __name__ == "__main__":
    ventana_fichero()