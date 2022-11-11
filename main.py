# Variables
salir = False
opc = int(input("""Introduce una opción: 
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))

# Listas y/o diccionarios
usuarios = {"david":[89143,"lattanzio"]}

while salir == False:
    match opc:
        case 1:
            print("Ha escogido registrar un usuario")
            clave = input("Cuál es el nombre del usuario: ")
            for valor in range(0,4):
                valor = input("Escribe dni,apellido,pais,telefono ")
                usuarios[clave]=[valor]
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
                    for clave,valor in usuarios.items(): 
                        print("Nombre: ",clave,end=": ")
                        for dato in valor:
                            print(dato,end=" ")
                    opc = int(input("""

Introduce una opción: 
Opción 1: Registrar un usuario
Opción 2: Ver todos o un usuario
"""))
                case 2:
                    usuario = input()
                    if usuario == usuarios.keys():
                        for clave,valor in usuarios.items(): 
                            print("Nombre: ",clave,end=": ")
                            for dato in valor:
                                print(dato,end=" ")
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

