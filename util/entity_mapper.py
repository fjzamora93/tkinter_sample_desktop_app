from typing import Optional, Tuple
from models.EmpleadoDTO import EmpleadoDTO

def entity_to_dto(empleado: Tuple) -> EmpleadoDTO:
    return EmpleadoDTO(
        id=empleado[0],
        nombre=empleado[1],
        seg_social=empleado[2],
        pagas_extras=empleado[3],
        email=empleado[4],
        irpf=empleado[5],
        salario=empleado[6],
        telefono=empleado[7],
        puesto=empleado[8],
        departamento=empleado[9],
        genero=empleado[10],
        afiliacion=empleado[11],
        datos_bancarios=empleado[12],
        fecha_nacimiento=empleado[13],
        nif=empleado[14],
        direccion=empleado[15],
        fecha_inicio=empleado[16]
    )

