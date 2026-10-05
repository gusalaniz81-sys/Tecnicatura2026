# Desempaquetar una lista o lits Unpacking
def show(nombre, apellido):
    print(nombre+' '+apellido)
persona = ["Lisandro", "Alaniz"]
show(persona[0], persona[1]) #Pasamos uno por uno los datos de la lista a la función
show(*persona)# Esto es lo mismo que lo anterior pero le pasamos TODO JUNTO
persona2 =("Bastian",'Alaniz') # Desempaquetamos a travez de una tupla
show(*persona2)
persona3 = {"nombre":"Bastian", "apellido":"Alaniiz"}
show(**persona3)

numbers = [1, 2, 3, 4, 5, 6] #Aún con la lista vacia se ejecuta el ELSE
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la única manera que no se ejecute el ELSE
else:
    print('Esto se terminó')