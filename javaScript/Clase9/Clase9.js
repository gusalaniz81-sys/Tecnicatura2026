//Evitar repetir tu código
//Dry don´t repeat yourself
let days = 5;
switch (days){
    case 1:
        console.log('hoy es Lunes');
        break
    case 2:
        console.log('hoy es Martes');
        break;
    case 3:
        console.log('hoy es Miércoles');
        break;
    case 4:
        console.log('hoy es Jueves');
        break;
    case 5:
        console.log('hoy es Viernes');
        break;
    case 6:
        console.log('hoy es Sábado');
        break;
    case 7:
        console.log('hoy es Domingo')
        break;
    default:
        console.log("Error en el ingreso del día de la semana");
        break;
}

//Esta es la opcion mejorada
let days2 = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('out of range');        
    }
    return days2[n-1]
}
console.log(getDay(3));