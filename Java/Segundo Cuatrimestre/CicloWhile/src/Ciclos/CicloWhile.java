package Ciclos;

public class CicloWhile {

    public static void main(String[] args) {
        var conteo = 0; //Inferencia de tipos
        while (conteo < 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en 1 la variable
        }
        int i = 0;
        while (i < 5) {
            System.out.println(i);
            i++;
        }
        var suma = 0;
        for (var j = 1; j <= 5; j++) {
            suma = suma + j;
        }
        System.out.println("suma = " + suma);
    }
}
