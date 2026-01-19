
from app.services.crear_usuario import crear_usuario
from app.services.login import validar_usuario

def menu():
    while True:

        print("escoja una opcion: ")
        print("1. crear usuario: ")
        print("2. ingresar al sistema: ")
        print("3. salir: ")

        opc = int(input("ingrese una opcion"))

        if opc == 1:
            crear_usuario()
        elif opc == 2:
            validar_usuario()
        elif opc == 3:
            break
        else:
            print("ingrese una opcion valida")



if __name__ == "__main__":
    menu()