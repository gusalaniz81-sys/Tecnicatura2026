/*
Ejercicio 4: Pedir número hasta que se teclee uno negativo
y mostrar cuantos número se han introducido.
Realizar con clase JOptionPane
 */
package clase3;

import javax.swing.JOptionPane;

public class Ejercicio4_JOptionPane {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número: "));
        
        var contador = 0;

        while (numero >= 0){
            contador++;

            numero = Integer.parseInt(
                JOptionPane.showInputDialog("Ingrese otro número"));

        }
        JOptionPane.showMessageDialog(null, "El número "+numero+" finaliza el programa");
        JOptionPane.showMessageDialog(null,"Se introdujeron " + contador + " números");
    }
 
            
}
