usuarios_ejemplos = []
usuarios_api = []

def crear_usuario():

    usuario = {}
    print("Ingrese su nombre")
    nombre = input(">> ")

    print("Ingrese su apellido")
    apellido = input(">> ")

    print("Ingrese su nombre de usuario")
    nombre_usuario = input(">> ")

    print("Ingrese su dirección de e-mail")
    mail = input(">> ")

    print("Ingrese su contraseña")
    contraseña = input(">> ")

    print("Disfrute sus 30 días de prueba gratis!")

    usuario["Nombre:"] = nombre
    usuario["Apellido:"] = apellido
    usuario["Nombre de usuario:"] = nombre_usuario
    usuario["Dirección de e-mail:"] = mail
    usuario["Contraseña:"] = contraseña


    usuarios_api.append(usuario)
    print(usuarios_api)
    #despues borrar!!

crear_usuario()

def iniciar_sesion(nombre_usuario, contraseña):
    cuenta_encontrada = {}

    print("\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("\t\t Nombre de nuestra plataforma")
    print("\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    for u in usuarios_ejemplos:
        if u["usuario"] == nombre_usuario:
            print("El usuario existe")
            if u["contraseña"] == contraseña:
                print("El usuario está logeado")
                cuenta_encontrada = u

            else:
                print("Clave errónea!")

    return cuenta_encontrada

while True:
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su clave: ")

    cuenta = iniciar_sesion(user, password)

    print(cuenta)

    if cuenta != {}:
        opcion = ""

        while opcion != SALIR:
            opcion = fun_operaciones_disponibles()

            if opcion == ACRED_CA:
