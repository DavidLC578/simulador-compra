# Variables
salir = False
opc = int(input("""Introduce una opción: 
Opción 1: Registrar un usuario
"""))

# Listas y/o diccionarios
usuarios = {}

while salir == False:
    match opc:
        case 1:
            print("Ha escogido registrar un usuario")
            clave = input("Cuál es el nombre del usuario: ")
            for valor in range(0,4):
                valor = input("Escribe dni,apellido,pais,telefono ")
                usuarios[clave]=[valor]
            for clave,valor in usuarios.items():    
                print("Nombre: ",clave,"Valores: ",valor)

            opc = int(input("""Introduce una opción: 
Opción 1: Registrar un usuario
"""))
        case 2:
            print("2")
            salir = True



