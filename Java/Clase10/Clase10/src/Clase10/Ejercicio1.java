
package Clase10;
import java.util.Scanner;
public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int horasTotales, semanas, dias, horasRestantes;

        System.out.print("Ingrese el número total de horas: ");
        horasTotales = entrada.nextInt();

        semanas = horasTotales / 168; // 7 días * 24 horas

        horasRestantes = horasTotales % 168;

        dias = horasRestantes / 24;

        horasRestantes = horasRestantes % 24;

        System.out.println("Equivale a:");
        System.out.println(semanas + " semanas");
        System.out.println(dias + " días");
        System.out.println(horasRestantes + " horas");

        entrada.close();
    }
}
