package ClaseConstructor;
public class ClaseConstructor {
    int a;
    int b;
    
    //El constructor es un método especial
    public ClaseConstructor(){//Constructor 1
        System.out.println("Se está ejecutando este constructor numero uno");
    }    
    //Estamos viendo lo que se llama la sobre carga de  constructor
    public ClaseConstructor(int a, int b){ //Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor número dos");
    }    
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
