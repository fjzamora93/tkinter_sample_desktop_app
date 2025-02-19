import database.dbconnection as db
from util.entity_mapper import entity_to_dto
from typing import Optional, Tuple
from models import EmpleadoDTO

def add_employee(
    entry_nombre: str,
    entry_seg_social : str,
    entry_pagas_extras : str,
    entry_email : str,
    entry_irpf : str,
    entry_salario : str,
    entry_telefono : str,
    entry_puesto : str,
    entry_departamento : str,
    entry_genero : str,
    entry_afiliacion : str,
    entry_datos_bancarios : str,
    entry_fecha_nacimiento : str,
    entry_nif : str,
    entry_direccion : str,
    entry_fecha_inicio : str,
):
    """
    Hace una validación de los datos y los inserta en la base de datos. Si es una cadena vacía, asigna valores por defecto.
    """
    # Si hay una cadena vacía, asignamos un valor por defecto
    nombre = entry_nombre or 'No se ha proporcionado nombre'
    seg_social = entry_seg_social or 'xxxxxxxxx'
    pagas_extras = entry_pagas_extras or 0
    email = entry_email or 'example@example.com'
    irpf = entry_irpf or 0.0
    salario = entry_salario or 0.0
    telefono = entry_telefono or '666 666 666'
    puesto = entry_puesto or 'Puesto de trabajo'
    departamento = entry_departamento or 'Dpt. de trabajo'
    genero = entry_genero or 'No especificado'
    afiliacion = entry_afiliacion or 'xxxxxxxxx'
    datos_bancarios = entry_datos_bancarios or 'xxxxxxxxx'
    fecha_nacimiento = entry_fecha_nacimiento or '2000-01-01'
    nif = entry_nif or 'xxxxxxxx-x'
    direccion = entry_direccion or 'C/ Falsa, 123'
    fecha_inicio = entry_fecha_inicio or '2000-01-01'


    db.insertar_datos(
        nombre,
        seg_social,
        pagas_extras,
        email,
        irpf,
        salario,
        telefono,
        puesto,
        departamento,
        genero,
        afiliacion,
        datos_bancarios,
        fecha_nacimiento,
        nif,
        direccion,
        fecha_inicio
    )

def obtener_empleado():
    """
    Obtiene los datos del último empleado insertado en la base de datos y lo transforma en DTO.

    Returns:
        Optional[EmpleadoDTO]: Objeto DTO del empleado si existe, de lo contrario None.

    Ejemplo de uso:
    >>> from models import EmpleadoDTO

    >>> datos = (1, "Juan Pérez", "123456", 2, "juan@example.com", 15.0, 3000.0, "654321098", "Desarrollador", "IT", "M", "Sindicato X", "Cuenta XYZ", "1985-06-15", "12345678A", "Calle Falsa 123", "2020-01-10")
    >>> db.obtener_datos = lambda: datos
    >>> empleado = obtener_empleado()

    >>> isinstance(empleado, EmpleadoDTO.EmpleadoDTO) or empleado is None    
    True

    >>> empleado.nombre
    'Juan Pérez'

    >>> empleado.salario
    3000.0

    >>> isinstance(empleado.id, int)
    True

    >>> isinstance(empleado.pagas_extras, str)
    False

    >>> isinstance(empleado.fecha_nacimiento, str)
    True


    """
    return entity_to_dto(db.obtener_datos())

#PYTHONPATH=./ python3 /home/javier/Desktop/TrabajosUnir/DesarrolloInterfaces/controller/controller_empleado.py
# pydoc -w ./controller/controller_empleado.py
# wkhtmltopdf controller_empleado.html controller_empleado.pdf

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)