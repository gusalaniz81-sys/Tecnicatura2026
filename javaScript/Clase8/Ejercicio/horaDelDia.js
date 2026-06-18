let horaDia = 14;
let mensaje;
if(horaDia >= 6 && horaDia <=11){
    mensaje = "Good morning";
}
else if(horaDia >=12 && horaDia <= 16){
    mensaje = "Good afternoom";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Good evening";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Good nigth";
}
else{
    mensaje = "Valor incorrecto";
}
console.log(mensaje);