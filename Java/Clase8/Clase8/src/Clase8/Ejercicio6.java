package Clase8;

import java.util.Scanner;
public class Ejercicio6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo,luis,juan,total;
        System.out.println("Ingrese la cantidad de dinero de guilermo");
        guillermo = Float.parseFloat(entrada.nextLine());
        
        luis = guillermo /2;
        juan = (luis + guillermo) / 2;
        total = luis + guillermo + juan;
        System.out.println("\nEl dinero de Luis es: us$"+ luis);
        System.out.println("\nEl dinero de juan es: us$"+ juan);
        System.out.println("\nEl total de dinero entre los tres es: us$"+total);
    }
}
