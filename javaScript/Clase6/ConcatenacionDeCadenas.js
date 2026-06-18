var nombre = "Lisandro";
var apellido = " Alaniz";
var nombreCompleto = nombre +' '+apellido; //Primera concatenación
console.log(nombreCompleto);
var nombreCompleto2 = 'Lisandro'+' '+'Alaniz'; //Segunda concatenación
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izq a derecha. Lee el n° como String(str)
console.log(juntos);
juntos = nombre + (78 +17); //Aquí se puede diferenciar a travez de los paréntesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; //Tercera concatenación usando el operador simplificado
console.log(nombre);
