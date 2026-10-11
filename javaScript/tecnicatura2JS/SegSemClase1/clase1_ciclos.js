// while
let contador = 0;
while (contador < 3){
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo while");

//Do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo < 3);
console.log('Fin del ciclo do while')

//for
for(let contando = 0; contando < 3; contando++){
    console.log(contando)
}
console.log('Fin del ciclo for')

// Palabra reservada break
for(let contando = 0; contando < 10; contando++){
    if(contando % 2 == 0){
        console.log(contando);
        break; //Muestra todos los pares
    }
}
console.log('Termina el ciclo al encontrar el primer n° par')

//La palabra continue
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue; //Continuar a la siguiente iteración
    }
    console.log(contando);
}
console.log('Termina el ciclo')

//La palabra continue y Etiquetas Labels 
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue inicio; //Continuar a la siguiente iteración
    }
    console.log(contando);
}
console.log('Termina el ciclo')

//La palabra break y Etiquetas Labels 
inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        break inicio; //Continuar a la siguiente iteración
    }
    console.log(contando);
}
console.log('Termina el ciclo')

const frutas = ['banana', ' orange', 'apple']
for(let claves of frutas.keys()){
    console.log(claves)
}

const arr = [1, 2, 3, 4, 5, 6];
const [a, b, ...resto] = arr;
console.log(a);
console.log(b);
console.log(resto);