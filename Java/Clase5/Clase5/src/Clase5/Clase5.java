package Clase5;


public class Clase5 {
    public static void main(String[] args) {
        //Inferencia de tipos var y tipos primitivos
        var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //Las literales con el punto se transforman en tipo Double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);
        
        //Tipor variable Char
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
       
        char varCaracter ='\u0024'; //Indicamos en JAVA la asignación con el código Unicode
        System.out.println("varCaracter = " + varCaracter);        
        char varCaracterDecimal = 36; //Valor Decimal del juego de caracter Unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; // UN caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
       
        var varCaracter1 ='\u0024'; //Indicamos en JAVA la asignación con el código Unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36; //Valor entero y le asigna un tipo int
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; // UN caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
       
        int varEnteroChar ='$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);
    }
}
