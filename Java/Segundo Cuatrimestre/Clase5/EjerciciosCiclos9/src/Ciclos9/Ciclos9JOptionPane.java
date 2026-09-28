/*
Ejercicio 9: Pedir el día, mes y año de una fecha e indicar si la 
fecha es correcta. Suponinedo que todos los meses son de 
30 días.
 */
package Ciclos9;
import javax.swing.JOptionPane;
public class Ciclos9JOptionPane {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el dia: "));        
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el mes: "));        
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el año: "));
        
        if((dia != 0)&&(dia <=30)){
            if ((mes !=0)&&(mes <=12)){
                if ((anio != 0)&&(anio<=2026)){
                    JOptionPane.showInputDialog(null, "La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }
                else{
                    JOptionPane.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                }
            }
            else{
                JOptionPane.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");
            }
        }
        else{
            JOptionPane.showMessageDialog(null, "Fecha incorrecta, día incorrecto");
        }
    }    
}
