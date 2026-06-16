package Clase6;

import java.util.Scanner;
public class Clase6 {
    public static void main(String[] args) {
        //Tipos primitivos tipos booleanos
        boolean varBool = true;
        System.out.println("varBool = " + varBool);
        
        if (varBool){
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");
        }
        
        //Algoritmo: ¿Es mayor de edad?
        var edad =18;//Literal tener presente la iferencia de tipos
        //var adulto = edad >=18;//Esta es una expresión booleana
        if(edad >= 18){
            System.out.println("Eres mayor de edad");
        }
        else{
            System.out.println("Eres meonr de edad");
        } 
        
    }
 
}
