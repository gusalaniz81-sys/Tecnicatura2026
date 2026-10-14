let persona = {
    nombre: 'Lisandro',
    apellido: 'Alaniz',
    email: 'lichi@gmail.com',
    edad: 5,
    idioma: 'ita',
    get lang(){
        return this.idioma.toUpperCase(); //Convierte las minúsculas a matúsculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ //Método o función en Javascript
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){// Este es el método get
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    },
    
}
console.log('Comenzamos a utilizar el método get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el método get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);

function Persona3(nombre, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Gustavo', 'Alaniz', 'lichi@lichi');
padre.email = 'gus@gus';
padre.telefono ='5491132028713';
console.log(padre.nombreCompleto())
console.log(padre);

let madre = new Persona3('Yamila', 'Sabrin', 'yami@yami');
console.log(madre.nombreCompleto())
console.log(madre);

//Diferentes formas de crear objetos
//Caso objeto 1:
let miObjeto = new Object(); //Sintaxis formal
//Caso Objeto 2:
let miObjeto2 = {}; //Esta opción es breve y recomendada

//Caso String 1
let miCadena1 = new String('Hola'); //Sintaxis formal
//Caso String 2
let miCadena2 = 'Hola'; //Esta es la sintaxis simplificada y recomendada

//Caso con números 1
let miNumero = new Number(1); //Es formal no recomendable
//Caso con numeros 2
let miNumero2 = 1; //Sintaxis recomendable

//Caso boolean 1
let miBoolean1 = new Boolean(false); //Formal
//Caso boolean 2
let miBoolean2 = false;

//Caso Arreglos 1
let miArreglo1 = new Array(); //Formal
//Caso Arreglo 2
let miArreglo2 = [];

//Caso Function 1
let miFuncion = new function(){}; //TOdo después de new es considerado objeto
//Caso function 2
let miFuncion2 = function(){}; //Notación simplificada y recomendada

//Uso de prototype
Persona3.prototype.telefono = '26183838323';
console.log(padre);
console.log(madre.telefono);

madre.telefono = '549261383838'

//Uso de call
let persona4 = {
    nombre: 'Basti',
    apellido: 'Alaniz',
    nombreCompleto2: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}

let persona5 = {
    nombre: 'Gustavo',
    apellido: 'Villalba'
}
console.log(persona4.nombreCompleto2('Lic.', '1122334455'));
console.log(persona4.nombreCompleto2.call(persona5,'tio', '5491154545454'));

//Método Apply
let arreglo = ['Ing.', '1122334455'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));