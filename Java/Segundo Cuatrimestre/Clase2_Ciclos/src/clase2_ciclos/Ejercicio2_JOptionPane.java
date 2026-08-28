
package clase2_ciclos;

import javax.swing.JOptionPane;

public class Ejercicio2_JOptionPane {
    public static void main(String[] args) {

        int numero = Integer.parseInt(
                JOptionPane.showInputDialog("Ingrese un número"));
        while (numero != 0){
        if (numero > 0){
            System.out.println("El número "+numero+ " es positivo");
            JOptionPane.showMessageDialog(null, "El número "+numero+ " es positivo");
        } 
        else{
            System.out.println("El número "+numero+ " es negativo");
            JOptionPane.showMessageDialog(null, "El numero "+numero+" es negativo");
        }
            numero = Integer.parseInt(
                JOptionPane.showInputDialog("Ingrese otro número"));
    }   
        System.out.println("El número "+numero+" finaliza el programa");
        JOptionPane.showMessageDialog(null, "El número "+numero+" finaliza el programa");
    }
}
