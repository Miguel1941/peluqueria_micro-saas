from app.db.db import conectar
from app.segurity.pasword import hash_password

# se crea el usuario y se guarda en mysql automaticamente para seguridad

def crear_usuario():
    nombre = input("ingrese su nombre: ")
    apellido = input("ingrese su apellido")
    numero = input("ingrese su numero de telefono: ")
    correo = input("correo: ")
    password = input("contraseña: ")

    password_hash = hash_password(password)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("select id from usuario where correo = %s", (correo,))   # no permite ingresar un correo ya ingresado
    if cursor.fetchone():            
        print("El correo ya existe")
        conn.close()
        return


    cursor.execute(
        """
        INSERT INTO usuario (nombre, apellido, numero, correo, password, activo, rol)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (nombre, apellido, numero, correo, password_hash, True, "usuario")
    )

    conn.commit()
    conn.close()

    print("Usuario creado correctamente")


if __name__ == "__main__":
    crear_usuario()
