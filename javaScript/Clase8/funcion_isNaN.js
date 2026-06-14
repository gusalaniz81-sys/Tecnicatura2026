let miNumero = "18"; //es una cadena
console.log(typeof miNumero);
let edad = Number(miNumero);//ésta es una funcion
console.log(typeof edad);
//Funcion isNan
if(isNaN(edad)){//no es un número = is Not a Number(devuelve un bool)
    console.log("Esta variable no contiene solo números")
}
else{
    if(edad >=18){
    console.log("Puede votar");
    }
    else{
    console.log("Es demasiado joven para votar");
    }
}

