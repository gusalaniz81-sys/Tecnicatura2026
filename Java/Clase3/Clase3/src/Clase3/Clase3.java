package Clase3;


public class Clase3 {

    public static void main(String[] args) {
        //VAR - Inferencia de tipo Java
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableCadena2 =" + miVariableCadena2);
        //soutv + tab
        System.out.println("miVariableEntera2 =" + miVariableEntera2);

        //Regas para definir una variable en Java
        var usuario = "Gustavo";
        var titulo = "Tecnico";
        var union = titulo + " " + usuario;
        System.out.println("union =" + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + a + b);
        System.out.println(usuario + (a + b));

        //ejercicio: Carateres Especiales con JAVA
        var nombre = "Lisandro";
        System.out.println("Nueva linea: \n" + nombre);//Diagonal inversa + n
        System.out.println("Tabulacion:\t" + nombre);//Tabuladro
        System.out.println("\nNueva Linea: \n" + nombre);
        System.out.println("\t\t .:Menu:.");
        System.out.println("Retroceso: \b\b" + nombre);//Caracter de retroceso   
        System.out.println("Comillas Simples: \'" + nombre + "\'");
        System.out.println("Comillas dobles: \"" + nombre + "\"");
        
        

    }
}
