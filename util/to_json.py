import json
import util.entity_mapper as mapper
import models.EmpleadoDTO as EmpleadoDTO
from database.dbconnection import obtener_datos

def guardar_datos_json(nombre_archivo="empleados.json"):

    # Obtener los datos del último empleado
    empleado: EmpleadoDTO = mapper.entity_to_dto(obtener_datos())  
    if not empleado:
        print("No hay datos disponibles.")
        return
    
    empleado_info = {
        "nombre": empleado.nombre,
        "seg_social": empleado.seg_social,
        "pagas_extras": empleado.pagas_extras,
        "email": empleado.email,
        "irpf": empleado.irpf,
        "salario": empleado.salario,
        "telefono": empleado.telefono,
        "puesto": empleado.puesto,
        "departamento": empleado.departamento,
        "genero": empleado.genero,
        "afiliacion": empleado.afiliacion,
        "datos_bancarios": empleado.datos_bancarios,
        "fecha_nacimiento": empleado.fecha_nacimiento,
        "nif": empleado.nif,
        "direccion": empleado.direccion,
        "fecha_inicio": empleado.fecha_inicio
    }

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(empleado_info, archivo, ensure_ascii=False, indent=4)

    print(f"Datos guardados en {nombre_archivo}")
