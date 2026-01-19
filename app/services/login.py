
from app.db.db import conectar
from app.segurity.pasword import verificar_password


def validar_usuario():
    conn = conectar()
    cursor = conn.cursor()

    correo_ingresado = input("ingrese su usuario: ")
    password_ingresada = input("ingrese su contraseña: ")

    cursor.execute(
        "select * from usuario where correo = %s",
        (correo_ingresado,)
    )
    usuario = cursor.fetchone()

    if not usuario:
        print("usuario no existe")
        return

    password_hash_bd = usuario[5]

    if verificar_password(password_ingresada, password_hash_bd):
        print("bienvenido al sistema")
    else:
        print("contraseña incorrecta")


if __name__ == "__main__":
    validar_usuario()



    