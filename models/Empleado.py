from dataclasses import dataclass


@dataclass
class Empleado:
    id: int
    nombre: str
    seg_social: str
    pagas_extras: int
    email: str
    irpf: float
    salario: float
    telefono: str
    puesto: str
    departamento: str
    genero: str
    afiliacion: str
    datos_bancarios: str
    fecha_nacimiento: str
    nif: str
    direccion: str
    fecha_inicio: str
    