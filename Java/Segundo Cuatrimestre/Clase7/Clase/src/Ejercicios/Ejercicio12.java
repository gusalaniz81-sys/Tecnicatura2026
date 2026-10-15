/*
Pedir un número y calcular su factorial
Hacerlos en las dos clases, Scanner y JOptionPane
 */
package Ejercicios;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ejercicio12 {
    public static void main(String[] args) {
        //Scanner entrada = new Scanner(System.in);
        long factorial = 1;
        //System.out.println("Ingrese un número: ");
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        for(int i =1; i<= numero; i++)
            factorial *=i;
        System.out.println("El factorial del número ingresado es: "+factorial);
        JOptionPane.showInternalMessageDialog(null,"El factorial del número ingresado es: "+factorial);
    }
    

  
}
