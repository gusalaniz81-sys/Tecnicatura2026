
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    //Metodo
    public void sumarNumero(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConretorno(){
        int resultado = a + b;
        return resultado;
    }
    
    public int sumarConArgumento(int a, int b){
        this.a = a;  //El argunmento "a" se asigna al atributo this.a 
        this.b = b;
        //return a + b;
        return this.sumarConretorno();
    }
    
}
