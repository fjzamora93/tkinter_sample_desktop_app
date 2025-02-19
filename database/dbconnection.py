import sqlite3
from typing import Optional, Tuple

# CONEXIÓN A LA BASE DE DATOS
def conectar_db():
    """Establece conexión con la base de datos SQLite."""
    conexion = sqlite3.connect("empleados.db")
    return conexion

# CREACIÓN INICIAL DE TABLAS
def crear_tabla():
    """Crea la tabla empleados en la base de datos si no existe."""
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT DEFAULT 'No se ha proporcionado nombre',
            seg_social TEXT DEFAULT 'xxxxxxxxx',
            pagas_extras INTEGER DEFAULT 0,
            email TEXT  DEFAULT 'example@example.com',
            irpf REAL DEFAULT 0.0,
            salario REAL DEFAULT 0.0,
            telefono TEXT DEFAULT '666 666 666',
            puesto TEXT DEFAULT 'PUesto de trabajo',
            departamento TEXT DEFAULT 'Dpt. de trabajo',
            genero TEXT DEFAULT 'No especificado',
            afiliacion TEXT DEFAULT 'xxxxxxxxx',
            datos_bancarios TEXT DEFAULT 'xxxxxxxxx',
            fecha_nacimiento DATE DEFAULT '2000-01-01',
            nif TEXT  DEFAULT 'xxxxxxxx-x',
            direccion TEXT DEFAULT 'C/ Falsa, 123',
            fecha_inicio DATE DEFAULT '2000-01-01'
        );

    ''')
    conexion.commit()
    conexion.close()


def insertar_datos(nombre, seg_social, pagas_extras, email, irpf, salario, telefono, puesto, departamento, genero, afiliacion, datos_bancarios, fecha_nacimiento, nif, direccion, fecha_inicio):
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO empleados (nombre, seg_social, pagas_extras, email, irpf, salario, telefono, puesto, departamento, genero, afiliacion, datos_bancarios, fecha_nacimiento, nif, direccion, fecha_inicio)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nombre, seg_social, pagas_extras, email, irpf, salario, telefono, puesto, departamento, genero, afiliacion, datos_bancarios, fecha_nacimiento, nif, direccion, fecha_inicio))
    conexion.commit()
    conexion.close()


def obtener_datos() -> Optional[Tuple]:
    """

    Recupera los datos SOLO del último empleado registrado en la base de datos.

    Returns:
        Optional[Tuple]: Tupla con los datos del empleado si existe, de lo contrario None.

    Ejemplo de uso:
    >>> resultado = obtener_datos()
    >>> isinstance(resultado, tuple) or resultado is None
    True


    """
    conexion = conectar_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleados ORDER BY id DESC LIMIT 1")  
    empleado = cursor.fetchone()  
    conexion.close()
    return empleado

# Probar los tests:
#PYTHONPATH=./ python3 /home/javier/Desktop/TrabajosUnir/DesarrolloInterfaces/database/dbconnection.py
# pydoc -w ./database/dbconnection.py
# wkhtmltopdf dbconnection.html dbconnection.pdf

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)