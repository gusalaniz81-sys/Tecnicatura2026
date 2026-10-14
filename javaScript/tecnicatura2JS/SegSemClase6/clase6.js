//let persona3 = new Persona('Nicolas', 'Alaniz'); Esto no se debe hacer: Persona in not defined

class Persona{ //Clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
    get apellido(){
        return this._apellido;
    }
    set apellido(apellido){
        return this._apellido = this.apellido;
    }
    nombreCompleto(){
        return this._nombre+' '+this._apellido;
    }
}

class Empleado extends Persona{//Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido)
        this._departamento = departamento;
    }
    get departamento(){
        return this._departamento
    }
    set departamento(departamento){
        this._departamento = departamento
    }

    //Sobreescritura: Modificar el comportamiento de algun metodo refinidos en la clase PADRE
    nombreCompleto(){
        return super.nombreCompleto()+' '+this._departamento;
    }

}

let persona1 = new Persona('Lisandro', 'Alaniz');
console.log(persona1.nombre);
persona1.nombre = 'Bastian';
console.log(persona1.nombre);
//console.log(persona1);
let persona2 = new Persona('Yamila', 'sabrin');
console.log(persona2.nombre);
persona2.nombre = 'Lucila';
console.log(persona2.nombre);
//console.log(persona2);

let Empleado1 = new Empleado('Mia', 'Bertoa', 'Idioma');
console.log(Empleado1);
console.log(Empleado1.nombre);
console.log(Empleado1.nombreCompleto());