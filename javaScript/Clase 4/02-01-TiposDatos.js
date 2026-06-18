// Tipos de datos en JavaScript
/*
La sintaxis en lo que es comentario
es muy similar a la de Java
realmente diriamos que es identica
*/
//Tipo String
var nombre = "Lisandro"; 
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
//Tipo numérico
var numero = 3000;
console.log(numero);
//Tipo Object
var objeto = {
    nombre : "Lisandro",
    apellido : "Alaniz",
    telefono : "123456"
}
console.log(objeto);

//Tipos de datos boolean
var bandera = true;
console.log(bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

//Tipos de datos clase
class Persona{
	constructor(nombre,apellido){
		this.nombre = nombre;
		this.apellido = apellido;
	}
}
console.log(typeof Persona);




