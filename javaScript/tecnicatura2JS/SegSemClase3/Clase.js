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
    console.log(arguments.length);
}
miFuncion2(5, 7);

// toString
var miFuncionTexto = miFuncion2.toString();
console.log(miFuncionTexto);
