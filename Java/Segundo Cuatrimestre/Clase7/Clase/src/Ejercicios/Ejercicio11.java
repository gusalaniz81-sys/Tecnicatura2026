/*
Ejercicio11: Diseñar un programa que muestre el producto 
de los 10 primeros números impares
Hacerlo en JOptionPane
 */
package Ejercicios;

import javax.swing.JOptionPane;

public class Ejercicio11 {

    public static void main(String[] args) {
        long numero = 1;
        for (int i = 1; i <= 20; i += 2) {
            numero *= i;
        }
        JOptionPane.showMessageDialog(null,"El producto de los números "
                + "impares es: "+ numero);
    }
}
    

    
