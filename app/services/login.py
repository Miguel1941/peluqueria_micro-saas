
from app.db.db import conectar


def validar_usuario():
    conn = conectar()
    cursor = conn.cursor()

    correo_ingresado = input("ingrese su usuario: ")
    password_ingresada = input("inrgese su contraseña: ")

    cursor.execute(
        "SELECT * FROM usuario WHERE correo = %s AND password = %s",
        (correo_ingresado, password_ingresada)
    )
    usuario = cursor.fetchone() # fetchone solo devuelve una fila

    if usuario:
        print("bienvenido al sistema")
    else:
        print("usuario o contraseña incorrectos")

if __name__ == "__main__":
    validar_usuario()


    