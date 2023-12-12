import json
import sqlite3

def crear_tabla_si_no_existe(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS datos_sistema (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cpu REAL,
            memoria REAL,
            bytes_enviados INTEGER,
            bytes_recibidos INTEGER,
            temperatura TEXT,
            mac TEXT,
            fecha_hora TEXT
        )
    ''')
    conexion.commit()

def insertar_informacion_sistema(conexion, informacion):
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO datos_sistema (cpu, memoria, bytes_enviados, bytes_recibidos, temperatura, mac, fecha_hora)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        informacion['cpu'],
        informacion['memoria'],
        informacion['red']['bytes_enviados'],
        informacion['red']['bytes_recibidos'],
        json.dumps(informacion['temperatura']),
        informacion['mac'],
        informacion['fecha_hora']
    ))
    conexion.commit()

from Rendimiento1 import obtener_info_sistema

def consultar_datos_sistema(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM datos_sistema')
    datos = cursor.fetchall()
    return datos

conexion = sqlite3.connect('tu_base_de_datos.db')

crear_tabla_si_no_existe(conexion)

informacion = obtener_info_sistema()

insertar_informacion_sistema(conexion, informacion)

datos_consultados = consultar_datos_sistema(conexion)
for dato in datos_consultados:
    print(dato)

conexion.close()

