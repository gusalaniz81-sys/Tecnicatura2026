class Persona{ //Clase padre
    
    static contadorPersonas = 0; //Atributo estático
    //email = 'Valor default email'; //Atributo no estático   
    static get MAX_OBJ(){ //Este método simula una constante
        return 5; //Limita la cantidad de objetos a crear
    }
   
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
            this.idPersona = ++ Persona.contadorPersonas;
        }
        else{
            console.log('Se ha superado el máximo de objetos permitidos')
        }
        
        //console.log('Se incrementa el contador:'+Persona.contadorObjetosPersona);
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
        return this.idPersona+' '+ this._nombre+' '+this._apellido;
    }
    //Sobreescribiendo el método de la clase padre(Object)
    toString(){ //Regresa un string
        //Se está aplicando multiples formas en tiempo de ejecución
        //El método que se ejecuta depende si es una referencia de tipo padr o hija
        return this.nombreCompleto();
    }

    static saludar(){
        console.log("Saludos desde este método");
    }

    static saludar2(persona1){
        console.log(persona1.nombre+' '+persona1.apellido);
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

//Object.prototype.toString Esta esla manera de acceder a atributos de manera dinámica
console.log(Empleado1.toString());
console.log(persona1.toString());

//persona1.saludar(); no se utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(Empleado1);

//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona)

console.log(persona1.email);
console.log(Empleado1.email);
//console.log(Persona.email); No se puede acceder desde la clase

console.log(persona1.toString());
console.log(persona2.toString());
console.log(Empleado1.toString());
console.log(Persona.contadorPersonas);

let persona3 = new Persona('Yamila', 'Sabrin');
console.log(persona3.toString());
console.log(Persona.contadorPersonas);

console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10; No se puede modificar, ni alterar
console.log(Persona.MAX_OBJ);
let persona4 = new Persona('Gustavo', 'Alaniz');
console.log(persona4.toString());
let persona5 = new Persona('Hernan', 'Alaniz');
console.log(persona5.toString())
