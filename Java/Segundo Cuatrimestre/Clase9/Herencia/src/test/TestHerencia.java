
package test;

import domain.Cliente;
import domain.Empleado;
import java.util.Date;
        
public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Gustavo", 60000.0);
        System.out.println("empleado1 = " + empleado1);
        Date fecha1 = new Date(); 
        Cliente cliente1 = new Cliente(fecha1, true, "Lisandro", 'M', 5, "Libertad 2151");
        System.out.println("cliente1 = " + cliente1);
    }
    
}
