
package caja;

public class Caja { //Clase publica caja
    int ancho;
    int alto;
    int profundidad;
    //Métodos y Constructores (acciones)
    public Caja(){ //Constructor 1 = vacio
    }
    
    public Caja(int ancho, int alto, int profundidad){//Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;
    }
    
    public int calcularVolumen(){ //Metodo para calcular
        return ancho * alto * profundidad;
    }
    
}
