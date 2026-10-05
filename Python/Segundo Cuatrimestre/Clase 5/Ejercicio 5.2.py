# Ejercicio 11: Agenda telefónica
# Hacer un programa que simule una agenda de contactos.
# Crear un diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendrá el siguiente munú de opciones
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir

agenda = {}
while True:
    print('\t.:Menu:.')
    print("1. Ingrese nuevo contacto")
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Ingrese su opcion: '))
    match opcion:
        case 1:
            nombre = input('Ingrese nuevo contacto: ')
            telefono = input('Ingrese nuevo telefono: ')
            agenda[nombre] = telefono

        case 2:
            borrar_nombre = input('Ingrese el contacto a borrar: ')
            if borrar_nombre in agenda:
                del agenda[borrar_nombre]
            else:
                print('El nombre no existe')

        case 3:
            for nombre, telefono in agenda.items():
                print(nombre, telefono)
        case 4:
            print('Salir')
            break
        case _:
            print('Opción incorrecta')



