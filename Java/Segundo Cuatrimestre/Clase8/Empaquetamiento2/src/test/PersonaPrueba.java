
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Lisandro", 80.000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modificamos a traves de los métodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre ="Juan Ignacio" //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); //Error
        System.out.println("persona1 con su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 con su nombre modificado es: "+persona1.getSueldo());
        System.out.println("persona1 con su nombre modificado es: "+persona1.isEliminado());
        
        //Tarea: Crear otro objeto de tipo Persona, asigna de manera inicial
        //Imprimir, luego modificar sus valores y volver a imprimir
        
        Persona persona2 = new Persona("Yami", 100.000, true);
        System.out.println("persona2 su nombre es: "+persona2.getNombre());
        System.out.println("persona2 con su sueldo es: "+persona2.getSueldo());
        System.out.println("persona2 con su boolean modificado es: "+persona2.isEliminado());
        
        persona2.setNombre("Lucila");
        persona2.setSueldo(200.000);
        persona2.setEliminado(true);
         System.out.println("persona2 su nombre nuevamente es: "+persona2.getNombre());
        System.out.println("persona2 con su sueldo nuevamente modificado es: "+persona2.getSueldo());
        System.out.println("persona2 con su boolean nuevamente modificado es: "+persona2.isEliminado());
        
        //System.out.println("persona1: "+persona1.toString());
        System.out.println("persona1 = " + persona1);
    }
}
