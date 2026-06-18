//Convertir String a Number
let miNumero = "18"; //es una cadena
console.log(typeof miNumero);
let edad = Number(miNumero);//ésta es una funcion
console.log(typeof edad);
if(edad >=18){
    console.log("Puede votar");
}
else{
    console.log("Es demasiado joven para votar");
}
//Operador ternario
let resultado = edad >=18 ? "Puede votar" : "Es muy joven";
console.log(resultado);

//Funcion isNan