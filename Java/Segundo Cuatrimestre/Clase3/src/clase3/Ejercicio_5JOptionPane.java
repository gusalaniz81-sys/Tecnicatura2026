/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package clase3;

import javax.swing.JOptionPane;

public class Ejercicio_5JOptionPane {

    public static void main(String[] args) {
        var numeroAleatorio = (int) (Math.random() * 101);
        var intentos = 0;

        var numero = Integer.parseInt(
                JOptionPane.showInputDialog("Ingrese un número entre 0 y 100:")
        );

        while (numero != numeroAleatorio) {

            intentos++;

            if (numero < numeroAleatorio) {
                JOptionPane.showMessageDialog(null, "El número es mayor");
            } else {
                JOptionPane.showMessageDialog(null, "El número es menor");
            }

            numero = Integer.parseInt(
                    JOptionPane.showInputDialog("Ingrese otro número:")
            );
        }

        intentos++;

        JOptionPane.showMessageDialog(
                null,
                "¡Acertaste!\n"+ "El número era: " + numeroAleatorio + "\n"
                
                + "Cantidad de intentos: " + intentos);
    }

}
