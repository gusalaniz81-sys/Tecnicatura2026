
package clase4;

public class ClasePersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Lisandro";
        persona1.apellido = "Alaniz";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Gustavo";
        persona2.apellido = "Alaniz";
        persona2.obtenerInformacion();
    }
}
