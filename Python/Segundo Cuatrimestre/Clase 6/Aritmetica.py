class Aritmetica:
    """
    el nombre de este tipo de comentario es: DocString
    esto es de documentación de la clase pytho
    Vamos a hacer en esta clase algunas operaciones de : suma, resta, mutilplicaión y mas
    """
    def __init__(self, operadndoA, operadndoB):
        self.operadndoA = operadndoA
        self.operadndoB = operadndoB
    #Método para sumas
    def sumar(self):
        return self.operadndoA + self.operadndoB

    def resta(self):
        return self.operadndoA - self.operadndoB

    def multiplicar(self):
        return self.operadndoA * self.operadndoB

    def dividir(self):
        return self.operadndoA / self.operadndoB
aritmetica = Aritmetica(7, 9 ) #Le pasamos los argunmentos para los operando
print(f'la sumas de los números es: {aritmetica.sumar()}')

print(f'La resta de los números es: {aritmetica.resta()}')
print(f'La multiplicacion de los números es: {aritmetica.multiplicar()}')
print(f'La divicion de los números es: {aritmetica.dividir():.2f}')

