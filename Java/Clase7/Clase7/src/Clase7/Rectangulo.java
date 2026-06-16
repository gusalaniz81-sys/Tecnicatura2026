package Clase7;


import java.util.Scanner;


public class Rectangulo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Ingrese la base del rectangulo");
        double base = scanner.nextDouble();
        
        System.out.println("Ingrese la altura del rectangulo");
        double altura = scanner.nextDouble();
        
        double area = base * altura;
        double perimetro = 2 * (base * altura);
        System.out.println("area: " + area);
        System.out.println("perimetro: " + perimetro);
        
        scanner.close();
        
    }

}
