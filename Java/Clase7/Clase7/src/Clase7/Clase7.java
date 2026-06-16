package Clase7;


public class Clase7 {

    public static void main(String[] args) {
//        int num1 = 5, num2 = 4;
//        var solucion = num1 + num2;
//        System.out.println("solucion de la suma = " + solucion);
//        
//        solucion = num1 - num2;
//        System.out.println("solucion de la resta = " + solucion);
//        
//        solucion = num1 * num2;
//        System.out.println("solucion de la multiplicación = " + solucion);
//        
//        solucion = num1 / num2;
//        System.out.println("solucion de la división = " + solucion);
//        
//        var solucion2 = 3.4 / num2;
//        System.out.println("solucion2 resultado de la división = " + solucion2);
//        
//        solucion = num1 % num2;//Guarda el residuo entero de la solución
//        System.out.println("solucion2 = " + solucion2);
//        
//        if(num2 %2 == 0)
//            System.out.println("Es un número Par");
//        else
//            System.out.println("Es un número Impar");
//        
//        //Operador de asignacion
//        int varNum1 = 1, varNum2 =4;
//        var varNum3 = varNum1 + 6 - varNum2; //Una operación
//        System.out.println("varNum3 = " + varNum3);
//        
        ////Operador de composicion
//        varNum1 +=1; //varNum1 = varNum1 + 1;
//        System.out.println("varNum1 = " + varNum1);        
//        varNum2 -=2; //varNum1 = varNum1 - 1;
//        System.out.println("varNum2 = " + varNum2);        
//        varNum1 *=5; //varNum1 = varNum1 * 1;
//        System.out.println("varNum1 = " + varNum1);        
//        varNum3 /=4; //varNum1 = varNum1 / 1;
//        System.out.println("varNum3 = " + varNum3);
//        varNum1 %= 6; //varNum1 = varNum1 + 1;
//        System.out.println("varNum1 = " + varNum1);
//        
           //Operadores Unarios = Cambio de signos
//           var varA = 7;
//        var varB = -varA;
//        System.out.println("varA = " + varA);
//        System.out.println("varB = " + varB);//El resultado será un número negativo
//
//        //Operador de negación
//        var varC = true; //Esta literal por default en Java es de tipo boolean
//        var varD = !varC; //Aquí esta invirtiendo el valor
//        System.out.println("varC = " + varC);
//        System.out.println("varD = " + varD);
//
//        //Operadores Unarios de Incremento: Preincremento
//        var varE = 9; //Se va a modificar su valor
//        var varF = ++varE; //Simbolo antes de la variable
//        //Primero se incrementa la variable y después se usa su valor
//        System.out.println("varE = " + varE);
//        System.out.println("varF = " + varF);
//
//        //PostIncremento (el simbolo va despué de la variable)
//        var varG = 3;
//        var varH = varG++;//Primero el valor d ela variable, luego el incremento
//        System.out.println("varG = " + varG);
//        System.out.println("varH = " + varH);
//        
//        //Operadores Unarios de decremento: Predecremento
//        var varI =4;
//        var varJ = --varI;
//        System.out.println("varI = " + varI);//La variable ya etá con decremento
//        System.out.println("varJ = " + varJ);
//        
//        //PostDecremento
//        var varK = 8;
//        var varL = varK--;//Primero el valor de la variable, luego quedael decremento
//        System.out.println("varK = " + varK);
//        System.out.println("varL = " + varL);
        
        //Operadores de Igualdad y Relacionales(Booleans)
//        var aNum = 5;
//        var bNum = 4;
//        var cNum = (aNum == bNum);
//        System.out.println("cNum = " + cNum);
//
//        var dNum = aNum != bNum;
//        System.out.println("dNum = " + dNum);
//
//        var cadenaA = "Hello";
//        var cadenaB = "bye bye";
//        var cVar = cadenaA == cadenaB;
//        System.out.println("cVar = " + cVar);
//
//        var fVar = cadenaA.equals(cadenaB);
//        System.out.println("fVar = " + fVar);
//
//        var gVar = aNum >= bNum;//> >= < <= == !=
//        System.out.println("gVar = " + gVar);
//
//        if (aNum % 2 == 0) {
//            System.out.println("El número es par");
//        }    else{
//            System.out.println("El número es Impar");
//        }
//        var edad = 30;
//        var adulto = 18;
//        if(edad >= adulto){
//            System.out.println("Es mayor de edad");
//        }
//        else{
//            System.out.println("Es menor de edad");
//        }
//        
//        //Operadores condicionales (and y or)
//        var valorA = 7;
//        var valorMinimo = 0; //Rango del 0 al 10
//        var valorMaximo = 10;
//        var respuesta = valorA >= 0 && valorA <= 10;
//        
//        if(respuesta){
//            System.out.println("Está dentro del rango");
//        }
//        else{
//            System.out.println("Está fuera dSel rango");
//        }
//        
//        //Operador or (||= or)
//        var vacaciones = false;
//        var diaLibre = true;
//        if(vacaciones || diaLibre){
//            System.out.println("Papá puede asistir al juego de su hijo");
//        }
//        else{
//            System.out.println("Papá no puede asistir al juego de su hijo");
//        }
        
        //Operador Ternario(Se recomienda con expresiones cortas o sencillas de dos lineas)
        /*var resultadoT = (5 > 8) ? "verdadero" : "falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 4;
        resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es Impar";
        System.out.println("resultadoT = " + resultadoT);*/
        
        var x =5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);//6
        System.out.println("y = " + y);//9
        System.out.println("z = " + z);//16
        
        var solucionAritmetica = 4 + 5 * 6 /3;// 4+((5*6)/3)
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
    }

}
