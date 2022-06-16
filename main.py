from crear_usuarios import crear_usuario
from iniciar_sesion import iniciar_sesion

def menu_plataforma():
    while True:
        print("Bienvenid@ a ___algo___")
        print("\t(1) Iniciar Sesión")
        print("\t(2) Registrarme")
        print("\t(3) Salir")

        option = input("¿Qué desea hacer? >> ")

        if option == "1":
            user = input("Ingrese su usuario: ")
            password = input("Ingrese su clave: ")

            iniciar_sesion(user, password)

        elif option == "2":
            crear_usuario()

        else:
            break

menu_plataforma()