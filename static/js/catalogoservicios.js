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
    // Pausa la animacion de giro
    'mouseenter': stopCarrusel,
    // Reanuda la funcion del giro
    'mouseleave': startCarrusel
});

// Comienza el efcto de giro al iniciar la pagina
startCarrusel();

const carousel = document.querySelector(".content-carrousel")
let isDragging = false;
const sensitivity = 5;
let cal = 0;

const dragStart = (e) =>{
    isDragging = true;
    const x = e.pageX || e.touches[0].pageX;
    carousel.classList.add("dragging");
    function rotation(e){
        const currentX = e.pageX || e.touches[0].pageX;
        cal = (currentX - x)/sensitivity;
        // Mejorar calculo, tiene la suma entre cal y currdeg, tiene que ser multiplo de 40
        carousel.style.transform = `rotateY(${cal+currdeg}deg)`
        console.log((cal+currdeg));
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
const dragStop = (e) =>{
    isDragging = false;
    carousel.classList.remove("dragging");
};
carousel.addEventListener("mousedown",dragStart);
carousel.addEventListener("touchstart",dragStart);
//-----------------------------------------------------------------------------------------------------------