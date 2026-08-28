/*
Ejercicio 4: Pedir número hasta que se teclee uno negativo
y mostrar cuantos número se han introducido.
Lo hacemos con la clase Scanner
Luego lo hacemos con la clase JOptionPane
 */
package clase3;

import java.util.Scanner;

public class Ejercicio_4 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingrese un número: ");
        var numero = Integer.parseInt(entrada.nextLine());

        var contador = 0;

        while (numero >= 0){
            contador++;

            System.out.println("Ingrese otro número: ");
            numero = Integer.parseInt(entrada.nextLine());

        }
        System.out.println("El número " + numero + " finaliza el programa");
        System.out.println("Se introdujeron " + contador + " números");
    }

}
