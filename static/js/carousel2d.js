// Service and team carousel
$(".service-carousel, .team-carousel").owlCarousel({
    autoplay: false,
    smartSpeed: 1500,
    margin: 30,
    dots: false,
    loop: true,
    nav : true,
    navText : [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0:{
            items:1
        },
        576:{
            items:1
        },
        768:{
            items:2
        },
        992:{
            items:3
        }
    }
});
$(document).ready(function(){
    $('.product-carousel').owlCarousel({
        loop: true,
        margin: 8, /* Reducir el margen entre elementos */
        nav: true, // Habilita las flechas de navegación
        navText: ['<span>&#9664;</span>', '<span>&#9654;</span>'], // Personaliza las flechas
        autoplay: true, // Desliza automáticamente
        autoplayHoverPause: true, // Pausa al pasar el ratón por encima
        responsive: {
            0: {
                items: 1
            },
            900: {
                items: 3
            },
            1000: {
                items: 5
            }
        }
    });
});