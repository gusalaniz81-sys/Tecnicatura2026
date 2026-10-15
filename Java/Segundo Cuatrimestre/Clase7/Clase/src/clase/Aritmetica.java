package clase;

public class Aritmetica {

    //Atributos de la clase
    int a;
    int b;

    //El constructor es un método especial
    public Aritmetica() { //Constructor vacio
        System.out.println("Se esta ejecutando este constructor numero uno");
    }

    ;
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){ //Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutando este constructos número dos");
    }
    
    //Metodo
    public void sumarNumero(){
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    
    public int sumarConRetorno(){
        int resultado = a + b;
        return resultado;
    }
    
    
    public int sumarConArgumento(int a, int b){
        this.a = a;
        this.b = b;
        return this.sumarConRetorno();
    }

}
