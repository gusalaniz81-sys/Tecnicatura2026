let x = 10; //Variable de tipo primitiva
console.log(x.length);
console.log('Tipos Primitivos');

// Objeto
let persona = {
    nombre: 'Lisandro',
    apellido: 'Alaniz',
    email: 'lichi@gmail.com',
    edad: 5,
    nombreCompleto: function(){ //Método o función en Javascript
        return this.nombre+' '+this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');

let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Basti';
persona2.direccion = 'Mazza 3100';
persona2.telefono = '5491135353131'
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');

console.log(persona['apellido']); //Accedemos como si fuera un arreglo

console.log('Usamos el ciclo for in')
//for in
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

console.log('Cambiamos y eliminamos un eror');
persona.apellida = 'Sabrin'; //Cambiamos dinamicamente un valor del objeto
delete persona.apellida; //eliminamos el error 
console.log(persona);

//Distintas formas de imprimir un objeto
//Número 1: La más sencilla, concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto: forma 1');
console.log(persona.nombre+' '+persona.apellido)

//Número 2: A travez del ciclo for in
console.log('Distintas formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero3: La función Object.values()
console.log('Distintas formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

// Número 4: Utilizamos el método JSON.stringify
console.log('Distintas formas de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);