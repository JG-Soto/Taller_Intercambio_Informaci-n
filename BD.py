import json
import mysql.connector
from Rendimiento1 import obtener_info_sistema

def crear_tabla_si_no_existe(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS datos_sistema (
            cpu FLOAT,
            memoria FLOAT,
            red INT,
            temperatura TEXT,
            mac VARCHAR(255),
            fecha_hora DATETIME
        )
    ''')
    conexion.commit()

def insertar_informacion_sistema(conexion, informacion):
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO datos_sistema (cpu, memoria, red, temperatura, mac, fecha_hora)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (
        informacion['cpu'],
        informacion['memoria'],
        informacion['red'],  # Si 'informacion['red']' es el valor de bytes enviados
        json.dumps(informacion['temperatura']),
        informacion['mac'],
        informacion['fecha_hora']
    ))
    conexion.commit()

def consultar_datos_sistema(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM datos_sistema')
    datos = cursor.fetchall()
    return datos

# Configurar la conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="mysql-grupo2.alwaysdata.net",
    user="grupo2",
    password="UCE2024",
    database="grupo2_metadatos"
)

# Verificar si la conexión fue exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos MySQL")

    # Crear tabla si no existe
    crear_tabla_si_no_existe(conexion)

    # Obtener información del sistema
    informacion = obtener_info_sistema()

    # Insertar información en la base de datos
    insertar_informacion_sistema(conexion, informacion)

    # Consultar datos de la base de datos
    datos_consultados = consultar_datos_sistema(conexion)
    for dato in datos_consultados:
        print(dato)

    # Cerrar la conexión
    conexion.close()
    print("Conexión cerrada")
else:
    print("Error al conectar a la base de datos MySQL")
