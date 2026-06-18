//HOy ya no se usa var, se utiliza let y const
let nombre = "Gustavo";
console.log(nombre)

const apellido2 = 'Alaniz';
//apellido2 = "gomes"; ##Una constante no puede ser modificada##
console.log(apellido2)


//###Ampliando el uso de var let y const###
/*
Con var puedes reasignar en cualquier momento
este forma parte del ámbito global
Un error es que se sobreescriba
*/
var nombre2 = 'Lisandro';
nombre2 = 'Gustavo';
console.log(nombre2);

function saludar(){
    var nombre5 ='Yamila';
    console.log(nombre5);
}
//console.log(nombre5)//Aquí no lee el dato de la funcion

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la funcion funciono correctamente, en la estructura if fallo
/*
Let: ésta puede ser reasignada en cualquier momento
la diferencia es que su ámbito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

function saludar2(){
    let nombre3 = 'Lisandro';
    console.log(nombre3) 
}
//console.log(nombre3)

if(true){
    let edad2 = 43;
    console.log(edad2);
}
//console.log(edad2);
/*
const se utiliza para valores constantes que no pueden ser reasignados
*/

const fechaNacimiento = 2021;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //Solo se ejecuta el console anterior