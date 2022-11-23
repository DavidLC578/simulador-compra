# Variables
salir = False
opc = int(input("""Introduce una opción:
1: Registrar un usuario
2: Ver todos o un usuario
3: Registrar una compra en un usuario
4: Ver una compra de un usuario
5: Salir del programa
"""))

# Listas y/o diccionarios
usuarios = {}
compras = {}

# Bucle principal
while salir == False:
    match opc:
        # En el caso uno se registra un nuevo usuario
        case 1:
            print("Ha escogido registrar un usuario")
            dni = int(input("Cuál es el dni del usuario: "))
            nombre = input("Escribe el nombre: ")
            apellido = input("Escribe el apellido: ")
            pais = input("Escribe el pais: ")
            telefono = input("Escribe el telefono: ")
            usuarios[dni] = [nombre, apellido, pais, telefono]
            opc = int(input("""

Introduce una opción:
1: Registrar un usuario
2: Ver todos o un usuario
3: Registrar una compra en un usuario
4: Ver una compra de un usuario
5: Salir del programa
"""))
        # En este caso dos, se daría dos opciones: ver todos los usuarios o ver sólo uno en concreto
        case 2:
            # Aquí se pide una nueva opción para elegir si ver todos o un usuario
            opc2 = int(input("""

Para ver todos o varios usuarios:
1: Ver todos
2: Ver un usuario
"""))   
            match opc2: 
                # Esta opción uno es para ver todos los usuarios registrados
                case 1:
                    for clave, valor in usuarios.items():
                        print("DNI: ", clave, end=": ")
                        for dato in valor:
                            print(dato, end=" ")
                    opc = int(input("""

Introduce una opción:
1: Registrar un usuario
2: Ver todos o un usuario
3: Registrar una compra en un usuario
4: Ver una compra de un usuario
5: Salir del programa
"""))
                # Con la opción dos se ve un usuario en concreto
                case 2:
                    usuario = int(
                        input("Introduce el dni de un usuario para ver sus datos: "))
                    if usuario in usuarios.keys():
                        print(usuario, end=": ")
                        for dato in usuarios[usuario]:
                            print(dato, end=" ")

                    opc = int(input("""

Introduce una opción:
1: Registrar un usuario
2: Ver todos o un usuario
3: Registrar una compra en un usuario
4: Ver una compra de un usuario
5: Salir del programa
"""))
                case _:
                    opc = int(input("""
Introduce una opción: 
1: Registrar un usuario
2: Ver todos o un usuario
3: Registrar una compra en un usuario
4: Ver una compra de un usuario
5: Salir del programa
"""))
        case 3:
            print("Ha escogido registrar una compra")
            idcompra = int(input("Escribe el numero de compra: "))
            dni2 = int(input("Cuál es el dni del usuario: "))
            productos = []
            cantp = int(
                input("Introduce la cantidad de productos que quieres registrar: "))
            print("Introduce los productos")
            for i in range(0, cantp):
                producto = input("Introducir producto: ")
                precio = int(input("El precio sería: "))
                productos.append([producto,precio])
            compras[idcompra] = [dni2, productos]
            opc = int(input(""" 

Introduce una opción: 
1: Registrar un usuario
2: Ver todos o un usuario
3: Registrar una compra en un usuario
4: Ver una compra de un usuario
5: Salir del programa
"""))
        case 4:
            print("Ha escogido ver una compra")
            compra = int(input("Introduce número de compra: "))
            if compra in compras.keys():
                print(compra, end=": ")
                print(compras[compra][0],end=", ")
                dni = compras[compra][0]
                if dni in usuarios:
                    print(usuarios[dni][0],end=", ")
                for datos in compras[compra][1]:
                    for dato in datos:
                        print(dato,end=" ")
            opc = int(input(""" 

Introduce una opción: 
1: Registrar un usuario
2: Ver todos o un usuario
3: Registrar una compra en un usuario
4: Ver una compra de un usuario
5: Salir del programa
"""))
        case _:
            print("Ha salido del programa")
            salir = True



