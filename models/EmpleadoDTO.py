

class EmpleadoDTO:
    def __init__(self, id: int, nombre: str, seg_social: str, pagas_extras: int, email: str, irpf: float, salario: float, telefono: str, puesto: str, departamento: str, genero: str, afiliacion: str, datos_bancarios: str, fecha_nacimiento: str, nif: str, direccion: str, fecha_inicio: str):
        self.__id = id
        self.__nombre = nombre
        self.__seg_social = seg_social
        self.__pagas_extras = pagas_extras
        self.__email = email
        self.__irpf = irpf
        self.__salario = salario
        self.__telefono = telefono
        self.__puesto = puesto
        self.__departamento = departamento
        self.__genero = genero
        self.__afiliacion = afiliacion
        self.__datos_bancarios = datos_bancarios
        self.__fecha_nacimiento = fecha_nacimiento
        self.__nif = nif
        self.__direccion = direccion
        self.__fecha_inicio = fecha_inicio

    def __repr__(self):
        return f"Empleado({self.__id}, {self.__nombre}, {self.__seg_social}, {self.__pagas_extras}, {self.__email}, {self.__irpf}, {self.__salario}, {self.__telefono}, {self.__puesto}, {self.__departamento}, {self.__genero}, {self.__afiliacion}, {self.__datos_bancarios}, {self.__fecha_nacimiento}, {self.__nif}, {self.__direccion}, {self.__fecha_inicio})"

    # Getters
    #! SOLO LECTURA, NO QUEREMOS QUE ANDEN MODIFICANDO LOS DATOS DE LOS EMPLEADOS
    @property
    def id(self) -> int:
        return self.__id

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def seg_social(self) -> str:
        return self.__seg_social

    @property
    def pagas_extras(self) -> int:
        return self.__pagas_extras

    @property
    def email(self) -> str:
        return self.__email

    @property
    def irpf(self) -> float:
        return self.__irpf

    @property
    def salario(self) -> float:
        return self.__salario

    @property
    def telefono(self) -> str:
        return self.__telefono

    @property
    def puesto(self) -> str:
        return self.__puesto

    @property
    def departamento(self) -> str:
        return self.__departamento

    @property
    def genero(self) -> str:
        return self.__genero

    @property
    def afiliacion(self) -> str:
        return self.__afiliacion

    @property
    def datos_bancarios(self) -> str:
        return self.__datos_bancarios

    @property
    def fecha_nacimiento(self) -> str:
        return self.__fecha_nacimiento

    @property
    def nif(self) -> str:
        return self.__nif

    @property
    def direccion(self) -> str:
        return self.__direccion

    @property
    def fecha_inicio(self) -> str:
        return self.__fecha_inicio



    @nombre.setter
    def nombre(self, value: str):
        self.__nombre = value

    @seg_social.setter
    def seg_social(self, value: str):
        self.__seg_social = value

    @pagas_extras.setter
    def pagas_extras(self, value: int):
        self.__pagas_extras = value

    @email.setter
    def email(self, value: str):
        self.__email = value

    @irpf.setter
    def irpf(self, value: float):
        self.__irpf = value

    @salario.setter
    def salario(self, value: float):
        self.__salario = value

    @telefono.setter
    def telefono(self, value: str):
        self.__telefono = value

    @puesto.setter
    def puesto(self, value: str):
        self.__puesto = value

    @departamento.setter
    def departamento(self, value: str):
        self.__departamento = value

    @genero.setter
    def genero(self, value: str):
        self.__genero = value

    @afiliacion.setter
    def afiliacion(self, value: str):
        self.__afiliacion = value

    @datos_bancarios.setter
    def datos_bancarios(self, value: str):
        self.__datos_bancarios = value

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, value: str):
        self.__fecha_nacimiento = value

    @nif.setter
    def nif(self, value: str):
        self.__nif = value

    @direccion.setter
    def direccion(self, value: str):
        self.__direccion = value

    @fecha_inicio.setter
    def fecha_inicio(self, value: str):
        self.__fecha_inicio = value