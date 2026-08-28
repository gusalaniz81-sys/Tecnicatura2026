/*
 Ejercicio 3: Leer número hasta que se introduzca un cero.
Para cada uno indicar si es par o impar.
Primero lo haremos con clase Scanner.
Luego con la clase JOptionPane
 */
package clase3;

import java.util.Scanner;

public class Ejercicio_3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un número: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0){
            if (numero %2 == 0){
                System.out.println("El número "+numero+ " es par");
        }   else{
                System.out.println("El numero "+numero+" es impar");
        }
        System.out.println("Ingrese otro número: ");
        numero = Integer.parseInt(entrada.nextLine());
    }   
        System.out.println("El número "+numero+" finaliza el programa");
    }

}
