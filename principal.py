import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter import *


from ventana_altas import *
from ventana_fichero import *

principal = tk.Tk() 
principal.title("Gestion de empleados")
principal.geometry("800x600+300+300")
principal.minsize(400,300)
principal.configure(bd=20)
principal.resizable(False,False)

marco = ttk.Frame(principal)
marco.pack(expand=True)

# Texto central
texto = tk.Label(marco, text="Holi, qué tal?", font=("Arial", 20))
texto.pack(pady=20)

try:
    imagen = PhotoImage(file="./public/assets/d20_dice.png")  
    imagen = imagen.subsample(int(imagen.width() // 130), int(imagen.height() // 150))
    imagen_label = tk.Label(marco, image=imagen)
    imagen_label.pack(pady=20)
except Exception as e:
    print("Error al cargar la imagen: ", e)


boton1 = ttk.Button(marco, text="Alta empleado", command=altas, style="TButton", width=60)
boton1.pack(pady=10)


boton2 = ttk.Button(marco, text="Generar Fichero", command=ventana_fichero, style="TButton", width=60)
boton2.pack(pady=10)


principal.mainloop() 
