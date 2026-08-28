/*
Ejercicio 5: Realizar un juego para adivinar un número, para ello
denerar un número aleatorio entre 0-100, y luego ir pidiendo números
indicando "es nayor " o "es menor" según sea mayor o menor con respecto
a N.
El proceso termina cuando el usuario acierta y mostamos el número de intentos
hechos.
 */
package clase3;

import java.util.Scanner;

public class Ejercicio5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        var numeroAleatorio = (int) (Math.random() * 101);
        var intentos = 0;

        System.out.println("Ingrese un número entre 0 y 100: ");
        var numero = Integer.parseInt(entrada.nextLine());

        while (numero != numeroAleatorio) {

            intentos++;

            if (numero < numeroAleatorio) {
                System.out.println("El número es mayor");
            } else {
                System.out.println("El número es menor");
            }

            System.out.println("Ingrese otro número: ");
            numero = Integer.parseInt(entrada.nextLine());
        }

        intentos++;

        System.out.println("¡Acertaste!");
        System.out.println("El número era: " + numeroAleatorio);
        System.out.println("Cantidad de intentos: " + intentos);
    }
}
