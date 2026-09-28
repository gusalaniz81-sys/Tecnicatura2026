
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumero();
        
        int resultado = aritmetica1.sumarConretorno();
        System.out.println("resultado = " + resultado);
        
        resultado = aritmetica1.sumarConArgumento(12, 26);
        System.out.println("resultado usando argumentos = " + resultado);
    }
}
