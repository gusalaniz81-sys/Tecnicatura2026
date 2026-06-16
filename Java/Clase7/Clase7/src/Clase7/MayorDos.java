package Clase7;


import java.util.Scanner;

public class MayorDos {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese el primero número");
        int num1 = scanner.nextInt();

        System.out.println("Ingrese el segundo número");
        int num2 = scanner.nextInt();

        int mayor = (num1 > num2) ? num1 : num2;
        
        System.out.println("El mayor es: " + mayor);

        scanner.close();
    }

}
