
package caja;


public class PruebaCaja {
    public static void main(String[] args) {
        //Variables Locales
        int medidaAncho = 4;
        int medidaAlto = 6;
        int medidaProf = 8;
        
        Caja caja1 = new Caja(); //Instanciamos el objeto, constructor vacio
        caja1.ancho = medidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundidad = medidaProf;
        int resultado = caja1.calcularVolumen(); //Llamamos al Método
        //Primer resultado
        System.out.println("Volumen de la caja 1 = " + resultado);
        
        Caja caja2 = new Caja(2, 4, 6); //Llamamos al constructor2 con nuevos Args
        //Llamamos con el nuevo objeto al método para otro calculo
        System.out.println("Volumen de caja 2: " + caja2.calcularVolumen());
    }
}
