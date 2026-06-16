package Clase10;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        double participacion, primerParcial, segundoParcial, examenFinal;
        double calificacionFinal;

        System.out.print("Ingrese la nota de participación: ");
        participacion = entrada.nextDouble();

        System.out.print("Ingrese la nota del primer parcial: ");
        primerParcial = entrada.nextDouble();

        System.out.print("Ingrese la nota del segundo parcial: ");
        segundoParcial = entrada.nextDouble();

        System.out.print("Ingrese la nota del examen final: ");
        examenFinal = entrada.nextDouble();

        calificacionFinal = (participacion * 0.10)
                          + (primerParcial * 0.25)
                          + (segundoParcial * 0.25)
                          + (examenFinal * 0.40);

        System.out.println("\nLa calificación final es: " + calificacionFinal);

        entrada.close();
    }
}
