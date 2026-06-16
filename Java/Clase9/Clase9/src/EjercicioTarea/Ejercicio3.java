package EjercicioTarea;

import java.util.Scanner;

public class Ejercicio3 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese dos números");
        var num1 = Double.parseDouble(entrada.nextLine());
        var num2 = Double.parseDouble(entrada.nextLine());
        Double resultado = null;
        if (num1 == num2) {
            resultado = num1 * num2;
        } else {
            if (num1 > num2) {
                resultado = num1 - num2;
            } else {
                resultado = num1 + num2;
            }
        }
        System.out.println("El resultado es = " + resultado);
    }
}
