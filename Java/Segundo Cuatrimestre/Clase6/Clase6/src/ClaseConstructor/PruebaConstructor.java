
package ClaseConstructor;
public class PruebaConstructor {
    public static void main(String[] args) {
        var a = 10; //Variable locales
        var b = 7;
        MiMetodo(); //Llamamos al método nuevo
        
        ClaseConstructor ClaseConstructor1 = new ClaseConstructor();
        ClaseConstructor1.a = 3;
        ClaseConstructor1.b = 7;
        ClaseConstructor1.sumarNumero();
        
        int resultado = ClaseConstructor1.sumarConretorno();
        System.out.println("resultado = " + resultado);
        
        resultado = ClaseConstructor1.sumarConArgumento(12, 26);
        System.out.println("resultado usando argumentos = " + resultado);  
        System.out.println("aritmetica1 a= " + ClaseConstructor1.a);
        System.out.println("aritmetica1 b = " + ClaseConstructor1.b);        
        ClaseConstructor ClaseConstructor2 = new ClaseConstructor(5, 8);
        System.out.println("aritmetica2 = " + ClaseConstructor2.a);
        System.out.println("aritmetica2 = " + ClaseConstructor2.b);
        
    }
    public static void MiMetodo(){
        int a = 10; //Una variable está limitada
        System.out.println("Aquí hay otro método");
    }
}
