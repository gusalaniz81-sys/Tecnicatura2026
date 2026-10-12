miFuncion(8, 2); //Esto se le conoce como hosting

function miFuncion (a, b){
    //console.log("Sumamos: "+ (a + b));
    return a + b; 
}

//Llamando a la funcion
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);

// Declaramos una función de tipo expresión
let x = function(a, b){return a + b}; //Necesita cierre con punto y coma
resultado = x(5,6) //al llamarla se pone la variable y paréntesis
console.log(resultado);

//Funciones de tipo self e invoking
(function(a, b){
    console.log("Ejecutar la funcion: "+ (a + b));
})(9, 6);

console.log(typeof miFuncion);
function miFuncion2(a, b){
    console.log(arguments)
    console.log(arguments.length);
}
miFuncion2(5, 7);

// toString
var miFuncionTexto = miFuncion2.toString();
console.log(miFuncionTexto);

//Funciones flechas
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3,7); //Asignamos el valor a una variable
console.log(resultado);

let sumar = function(a = 4, b = 8){
    console.log(arguments[0]);
    console.log(arguments[1]) // Muetra el parámetro de: a
    return a + b + arguments[2];
}
resultado = sumar(3, 2, 9);
console.log(resultado);

//Sumar todos los argumentos
let respuesta = sumarTodo(5 , 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for( let i = 0; i < arguments.length; i ++){
        suma += arguments[i]; //arguments es para arreglos
    }
    return suma;
}

//Tipos primitivos
let k = 10;
function cambiarValor(a){
    a = 20;
}
cambiarValor(k);
console.log(k);


//Paso por referencia
const persona = {
    nombre: "Lisandro",
    apellido: "Alaniz"
};
console.log(persona);

function cambiarValorObjeto(p1){
    p1.nombre = 'Yamila';
    p1.apellido = 'Sabrin';
}
cambiarValorObjeto(persona);
console.log(persona);