
import java.util.Scanner;

public class HolaMundo {

    public static void main(String[] args) {
        /*System.out.println("Hola Mundo desde Java");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programación";
        System.out.println(miVariableCadena);
         */

        //VAR - Inferencia de tipo Java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableCadena2 =" + miVariableCadena2);
        //soutv + tab
        System.out.println("miVariableEntera2 =" + miVariableEntera2);
         
        var usuario = "Gustavo";
        var titulo = "Tecnico";
        var union = titulo + " " + usuario;
        System.out.println("union =" + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + a + b);
        System.out.println(usuario + (a + b));
        var nombre = "Lisandro";
        System.out.println("Nueva linea: \n" + nombre);
        System.out.println("Tabulacion:\t" + nombre);
        System.out.println("\nNueva Linea: \n" + nombre);
        System.out.println("\t\t .Menu:.");
        System.out.println("Comillas Simples: \'"+nombre+"\'");
        System.out.println("Comillas dobles: \""+nombre+"\"");*/
        
        //Clase Scanner
        /*Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese su nombre");
        var usuario2 = entrada.nextLine();
        System.out.println("Usuario2 = " + usuario2);
        System.out.println("Escriba el título: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);*/
        
        /*
        byte numEnteroByte = 127;
        System.out.println("numEnteroByte= "+ numEnteroByte);
        System.out.println("Valor mínimo del Byte:" + Byte.MIN_VALUE);
        System.out.println("Valor máximo del Byte:" + Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = "+ numEnteroShort);
        System.out.println("Valor mínimo del short:" + Short.MIN_VALUE);
        System.out.println("Valor máximo del short:" + Short.MAX_VALUE); 
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = "+ numEnteroInt);
        System.out.println("Valor mínimo del int:" + Integer.MIN_VALUE);
        System.out.println("Valor máximo del int:" + Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = "+ numEnteroLong);
        System.out.println("Valor mínimo del int:" + Long.MIN_VALUE);
        System.out.println("Valor máximo del int:" + Long.MAX_VALUE);
        */
        /*float numFloat = 3.4028235E38F;
        System.out.println("numFloat: "+ numFloat);
        System.out.println("El valor mínimo de float:"+ Float.MIN_VALUE);
        System.out.println("El valor máximo de float:"+ Float.MAX_VALUE);
        
        double numDouble = 10;
        System.out.println("numDouble: "+ numDouble);
        System.out.println("El valor mínimo de double:"+ Double.MIN_VALUE);
        System.out.println("El valor máximo de double:"+ Double.MAX_VALUE);*/
       
        //Inferencia de tipos var y tipos primitivos
        /*var numEntero = 20; //Las literales sin punto automaticamente son de tipo int
        System.out.println("numEntero =" + numEntero);
        var numFloat = 10.0F; //Las literales con el punto se transforman en tipo Double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
       
        /*//Tipor variable Char
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
        var varCaracterDecimal1 = (char)36; //Valor Decimal del juego de caracter Unicode
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; // UN caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
       
        int varEnteroChar ='$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);*/
        
        //tipo primitivos tipos booleanos
        /*boolean varBool = false;
        System.out.println("varBool = " + varBool);
        
        if (varBool){
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");
        }
        
        //Algoritmo: ¿Es mayor de edad?
        var edad =18;//Literal tener presente la iferencia de tipos
        //var adulto = edad >=18;//Esta es una expresión booleana
        if(edad >= 18){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres meonr de edad");
        } */
        
        //Conversion de tipos primitivos
        /*var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("valorPI = " + valorPI);
        
        //pedir valor al usuario
        var entrada = new Scanner(System.in);
        System.out.println("Ingrese su edad");
        edad = Integer.parseInt( entrada.nextLine());
        System.out.println("edad =" + edad);*/
        
        //Conversión de tipo primitivos en Java Parte 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        
    }
}
