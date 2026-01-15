

import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root1234!",
        database="peluqueria"
    )

    if conexion.is_connected():
        print("✅ Conexión exitosa a la base de datos")
    else:
        print("❌ Falló la conexión")

    return conexion

conectar()