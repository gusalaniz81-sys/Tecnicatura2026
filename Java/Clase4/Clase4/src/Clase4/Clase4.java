package Clase4;


public class Clase4 {
    public static void main(String[] args) {
        byte numEnteroByte = 127;
        System.out.println("numEnteroByte= "+ numEnteroByte);
        System.out.println("Valor mínimo del Byte:" + Byte.MIN_VALUE);
        System.out.println("Valor máximo del Byte:" + Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = "+ numEnteroShort);
        System.out.println("Valor mínimo del short:" + Short.MIN_VALUE);
        System.out.println("Valor máximo del short:" + Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = "+ numEnteroInt);
        System.out.println("Valor mínimo del int:" + Integer.MIN_VALUE);
        System.out.println("Valor máximo del int:" + Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = "+ numEnteroLong);
        System.out.println("Valor mínimo del int:" + Long.MIN_VALUE);
        System.out.println("Valor máximo del int:" + Long.MAX_VALUE);
        
        float numFloat = 3.4028235E38F;
        System.out.println("numFloat: "+ numFloat);
        System.out.println("El valor mínimo de float:"+ Float.MIN_VALUE);
        System.out.println("El valor máximo de float:"+ Float.MAX_VALUE);
        
        double numDouble = 10;
        System.out.println("numDouble: "+ numDouble);
        System.out.println("El valor mínimo de double:"+ Double.MIN_VALUE);
        System.out.println("El valor máximo de double:"+ Double.MAX_VALUE);
    }
}
