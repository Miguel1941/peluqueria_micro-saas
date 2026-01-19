


import bcrypt


def hash_password(password: str): 
    password_bytes = password.encode("utf-8")   # Convierte el str a bytes
    salt = bcrypt.gensalt()  # crea varios hashead por seguridad
    hashed = bcrypt.hashpw(password_bytes, salt)  # crea el hash que se usa
    return hashed


def verificar_password(password_ingresado: str, password_bd: str):
    return bcrypt.checkpw(
        password_ingresado.encode("utf-8"),  # Convierte la contraseña ingresada a bytes
        password_bd.encode("utf-8") # guarda en mysql
    )
