# Variables
salir = False
opc = int(input("""Introduce una opción: 
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))

# Listas y/o diccionarios
usuarios = {}

while salir == False:
    match opc:
        case 1:
            print("Ha escogido registrar un usuario")
            dni = input("Cuál es el dni del usuario: ")
            nombre = input("Escribe el nombre: ")
            apellido = input("Escribe el apellido: ")
            pais = input("Escribe el pais: ")
            telefono = input("Escribe el telefono: ")

            usuarios[dni]=[nombre,apellido,pais,telefono]
            opc = int(input("""

Introduce una opción: 
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))
        case 2:
            # A partir de aquí se elige la opcion, ver todos los  usuarios o uno en concreto
            opc2 = int(input("""

Para ver todos o varios usuarios:
Opción 1: Ver todos
Opción 2: Ver un usuario
"""))
            match opc2:
                case 1:
                    # print(usuarios)
                    for clave,valor in usuarios.items(): 
                        print("DNI: ",clave,end=": ")
                        for dato in valor:
                            print(dato,end=" ")
                    opc = int(input("""

Introduce una opción: 
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))
                case 2:
                    usuario = input("Introduce el dni de un usuario para ver sus datos: ")
                    if usuario in usuarios:
                        for clave,valor in usuarios.items(): 
                            print("Nombre: ",clave,end=": ")
                            for dato in valor:
                                print(dato,end=" ")
                    opc = int(input("""

Introduce una opción: 
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))
                case _:
                    opc = int(input("""
Introduce una opción: 
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))
                    


# usuarios = {"wieur":[234132,"asdfasd"]}
# for clave, valor in usuarios.items():
#     print(clave,end=": ")
#     for dato in valor:
#         print(dato,end=" ")

