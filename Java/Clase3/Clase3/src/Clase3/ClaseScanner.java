package Clase3;


import java.util.Scanner;
public class ClaseScanner {
    public static void main(String[] args) {    
    
    //Clase Scanner
    Scanner entrada = new Scanner(System.in);
    System.out.println ("Ingrese su nombre");
    var usuario2 = entrada.nextLine();
    System.out.println ("Usuario2 = " + usuario2);    
    System.out.println ("Escriba el título: ");
    var titulo2 = entrada.nextLine();
    System.out.println ("Resultado: "+titulo2+" "+usuario2);
    }
}
