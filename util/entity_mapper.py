from typing import Optional, Tuple
from models.EmpleadoDTO import EmpleadoDTO


def entity_to_dto(empleado: Tuple) -> EmpleadoDTO:
    """
    Convierte una tupla con datos de empleado en un objeto EmpleadoDTO.

    Args:
        empleado (Tuple): Tupla con los datos del empleado.

    Returns:
        EmpleadoDTO: Objeto DTO del empleado.

    Ejemplo de uso:
    >>> datos = (1, "Juan Pérez", "123456", 2, "juan@example.com", 15, 3000, "654321098", "Desarrollador", "IT", "M", "Sindicato X", "Cuenta XYZ", "1985-06-15", "12345678A", "Calle Falsa 123", "2020-01-10")
    >>> empleado = entity_to_dto(datos)
    >>> isinstance(empleado, EmpleadoDTO)
    True
    >>> empleado.nombre
    'Juan Pérez'
    >>> empleado.salario
    3000
    >>> isinstance(empleado.id, int)
    True
    >>> isinstance(empleado.pagas_extras, str)
    False

    >>> empleado.salario = 1000

    >>> empleado = entity_to_dto(datos)
    >>> empleado.salario = 99999999  
    >>> empleado.salario
    100000

    >>> try:
    ...     empleado.salario = -1
    ... except ValueError as e:
    ...     print(e)
    El salario no puede ser negativo.

    """
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

# PYTHONPATH=./ python3 /home/javier/Desktop/TrabajosUnir/DesarrolloInterfaces/util/entity_mapper.py
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)