//---------------------------------------- Carrusel 3D animacion de rotacion ---------------------------------
var carrusel = $(".content-carrousel"), currdeg  = 0; // Inicio de la rotacion

function rotate(e){
    currdeg = currdeg - 40 // Indica el grado de la rotacion del carrusel, esto se ajusta a la cantidad de imagenes que se carge en el css
    carrusel.css({
        "-webkit-transform": "rotateY("+currdeg+"deg)",
        "-moz-transform": "rotateY("+currdeg+"deg)",
        "-o-transform": "rotateY("+currdeg+"deg)",
        "transform": "rotateY("+currdeg+"deg)"
    });
}

// storing state in window.carouselPause
const startCarrusel = (e) => window.carruselPause = setInterval(rotate, 3000); // Funcion para iniciar la animacion de giro
const stopCarrusel = (e) => clearInterval(window.carruselPause); // Funcion para parar la animacion

carrusel.on({
    // Pausa la animacion de giro, cuando el mouse esta sobre la ruleta
    'mouseenter': stopCarrusel,
    // Reanuda la funcion del giro, cuando el mouse sale de la ruleta
    'mouseleave': startCarrusel
});

// Comienza el efcto de giro al iniciar la pagina
startCarrusel();
//---------------------------------------- Carrusel 3D animacion de rotacion ---------------------------------

//---------------------------------------- Carrusel 3D animacion de arrastre ---------------------------------
const carousel = document.querySelector(".content-carrousel")// Obtengo el elemento que contiene el carrusel
let isDragging = false;//Bandera para indetificar si esta siendo arrastrado
const sensitivity = 5;//Sensibilidad del arrastre, sirve para calcular el grado de giro de la ruleta
let cal = 0;//Variable para calcular la posicion final

const dragStart = (e) =>{
    isDragging = true;
    const x = e.pageX || e.touches[0].pageX;
    carousel.classList.add("dragging");
    function rotation(e){
        const currentX = e.pageX || e.touches[0].pageX;
        cal = (currentX - x)/sensitivity;
        cal = Math.round(cal/40)*40; // Redondeo al multiplo mas cercano del 40
        carousel.style.transform = `rotateY(${cal+currdeg}deg)`
    }
    function endDrag(){
        currdeg += cal;
        
        carousel.removeEventListener("touchmove",rotation);
        carousel.removeEventListener("mousemove",rotation);
        window.removeEventListener("mouseup",endDrag);
        window.removeEventListener("touchend",endDrag);
    }
    carousel.addEventListener("mousemove",rotation);
    carousel.addEventListener("touchmove",rotation);
    window.addEventListener("mouseup",endDrag)
    window.addEventListener("touchend",endDrag)
};
const dragging = (e) =>{
    if(!isDragging) return;
    rotation(e);
    //console.log(e.pageX);
};
const dragStop = (e) =>{// Estado de desagarre
    isDragging = false;
    carousel.classList.remove("dragging");
};
carousel.addEventListener("mousedown",dragStart);
carousel.addEventListener("touchstart",dragStart);
//---------------------------------------- Carrusel 3D animacion de arrastre ---------------------------------

let acc = document.getElementsByClassName("accordion"); // Obtiene cada uno de los elementos que tengan la clase

for (let i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){ // Le agrega el evento onclick
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("show");
    }
}

//------------Fomulario------------//
document.getElementById('appointmentForm').addEventListener('submit', function(event) {
// Evita el envío del formulario para que no se recargue la página
event.preventDefault();

// Captura los valores de los campos del formulario los datos
const name = document.getElementById('inputName').value;
const email = document.getElementById('inputEmail').value;
const date = document.getElementById('inputDate').value;
const time = document.getElementById('inputTime').value;
const service = document.getElementById('serviceSelect').value;
const professional = document.getElementById('professionalSelect').value;

// Inserta los valores en el modal
document.getElementById('confirmName').textContent = name;
document.getElementById('confirmEmail').textContent = email;
document.getElementById('confirmDate').textContent = date;
document.getElementById('confirmTime').textContent = time;
document.getElementById('confirmService').textContent = service;
document.getElementById('confirmProfessional').textContent = professional;

//Muestra el modal de confirmación si esta oka 
$('#confirmationModal').modal('show');
});

// Cierra el modal cuando cierra
document.getElementById('closeModalButton').addEventListener('click', function() {
$('#confirmationModal').modal('hide');
});