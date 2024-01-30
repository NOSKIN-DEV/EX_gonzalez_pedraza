
$(function(){
    $("#miformulario").validate({
        rules:{
            nombre:{
                required:true,
            },
            apellido:{
                required:true, 
            },
            
            correo:{
                    required:true,
                    email:true,
                },
            
            
            
        },//Cierra el area de rules
        messages:{
            nombre:{
                required:"Ingrese nombre del usuario:",
                minlength:"Caracteres insuficientes (3)",
            },
            apellido:{
                required:"Ingrese el apellido",
                minlength:"Caracteres insuficientes (3)",
            },
            correo:{
                required:"Ingrese su correo electronico",
                email:"Formato de correo no valido",
            },
        }
    })
    
    
    
})
function cambiarColorNOM() {
    //cambio de la caja NOMBRE
    var nom = document.getElementById('nom');
    nom.style.backgroundColor = '#566573';
    nom.style.color = 'white';
    nom.style.border = '2px solid orange';
    
}
function restaurarDiseñoNOM() {
    // Obtener referencia al input
    var nom = document.getElementById('nom');
    // Restaurar el diseño original cuando pierde el foco
    nom.style.backgroundColor = '';
    nom.style.color = '';
    nom.style.border = '';
}//fin de cambio de color (nombre)

function cambiarColorAP() {
    //cambio de la caja (a_paterno)
    var ap = document.getElementById('a_paterno');
    ap.style.backgroundColor = '#566573';
    ap.style.color = 'white';
    ap.style.border = '2px solid orange';
}
function restaurarDiseñoAP() {
    // Obtener referencia al input
    var ap = document.getElementById('a_paterno');
    // Restaurar el diseño original cuando pierde el foco
    ap.style.backgroundColor = '';
    ap.style.color = '';
    ap.style.border = '';
}//fin de cambio de color (a_paterno)

function cambiarColorAM() {
    //cambio de la caja (a_materno)
    var am = document.getElementById('a_materno');
    am.style.backgroundColor = '#566573';
    am.style.color = 'white';
    am.style.border = '2px solid orange';
}
function restaurarDiseñoAM() {
    // Obtener referencia al input
    var am = document.getElementById('a_materno');
    // Restaurar el diseño original cuando pierde el foco
    am.style.backgroundColor = '';
    am.style.color = '';
    am.style.border = '';
}//fin de cambio de color (a_materno)

function cambiarColorCORREO() {
    //cambio de la caja (correo)
    var c = document.getElementById('correo');
    c.style.backgroundColor = '#566573';
    c.style.color = 'white';
    c.style.border = '2px solid orange';
}
function restaurarDiseñoCORREO() {
    // Obtener referencia al input
    var c = document.getElementById('correo');
    // Restaurar el diseño original cuando pierde el foco
    c.style.backgroundColor = '';
    c.style.color = '';
    c.style.border = '';
}//fin de cambio de color (correo)

function cambiarColorTELEFONO() {
    //cambio de la caja (fono)
    var f = document.getElementById('fono');
    f.style.backgroundColor = '#566573';
    f.style.color = 'white';
    f.style.border = '2px solid orange';
}
function restaurarDiseñoTELEFONO() {
    // Obtener referencia al input
    var f = document.getElementById('fono');
    // Restaurar el diseño original cuando pierde el foco
    f.style.backgroundColor = '';
    f.style.color = '';
    f.style.border = '';
}//fin de cambio de color (fono)

function cambiarColorTCONSULTA() {
    //cambio de la caja (fono)
    var t_con = document.getElementById('t_consulta');
    t_con.style.backgroundColor = '#566573';
    t_con.style.color = 'white';
    t_con.style.border = '2px solid orange';
}
function restaurarDiseñoTCONSULTA() {
    // Obtener referencia al input
    var t_con = document.getElementById('t_consulta');
    // Restaurar el diseño original cuando pierde el foco
    t_con.style.backgroundColor = '';
    t_con.style.color = '';
    t_con.style.border = '';
}//fin de cambio de color (fono)

function cambiarColorCON() {
    //cambio de la caja (fono)
    var con = document.getElementById('con');
    con.style.backgroundColor = '#566573';
    con.style.color = 'white';
    con.style.border = '2px solid orange';
}
function restaurarDiseñoCON() {
    // Obtener referencia al input
    var con = document.getElementById('con');
    // Restaurar el diseño original cuando pierde el foco
    con.style.backgroundColor = '';
    con.style.color = '';
    con.style.border = '';
}//fin de cambio de color (fono)
    
function limpiarForm() {
    // Obtener referencia al formulario
    var formulario = document.getElementById('miformulario');

    // Limpiar los campos del formulario
    formulario.reset();
  }
document.addEventListener('scroll', function() {
    var navbar = document.getElementById('navbar');
    
    if (window.scrollY > 1) {
      navbar.classList.add('superior');
    } else {
      navbar.classList.remove('superior');
    }
});
function tiemporeal()
{
    let date=new Date();
    let hh= date.getHours();
    let mm= date.getMinutes();
    let ss= date.getSeconds();

    hh= (hh < 10) ? "0" + hh : hh;
    mm= (mm < 10) ? "0" + mm : mm;
    ss= (ss < 10) ? "0" + ss : ss;

    let tiempo =hh+":"+mm+":"+ss;
    let reloj =document.querySelector('#reloj');
    reloj.innerHTML =tiempo;
}

setInterval(tiemporeal,1000);