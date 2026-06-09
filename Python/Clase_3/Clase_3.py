a = 10
print(type(a))
a = 10.78
print(type(a))

# Booleano
a = False
print(type(a))
b = True
print(type(b))

# Tipos int, float, String, Boot
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Mundo"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (Sting)
miGrupoFaborito = "Queen"
print("Mi Grupo favorito es: "+ miGrupoFaborito)

miGrupoFaborito = "Queen"+" "+"La mejor banda"
print("Mi Grupo favorito es: "+ miGrupoFaborito)
caracteristica = "The best Rock Band"
print("Mi Grupo favorito es: "+ miGrupoFaborito +" "+ caracteristica)
print("Mi Grupo favorito es: ", miGrupoFaborito, caracteristica)

numero1 = "7"
numero2 = "8"
print(numero1 + numero2)
print(int(numero1) + int(numero2)) #Convertimos los String a Entero
numero3 = 7
numero4 = 8
print(numero3 + numero4)
#print(int(numero3) + int(numero4)

#Tpos Boleanos (boll)
miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# Funcion --> input()
resultado = input("Ingrese un número: ") #Regresa un dato tipo String
print(resultado)

# Conversión de Datos
numero1 = int(input("Escribe el 1er número: "))
numero2 = int(input("escibe el 2do número: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)