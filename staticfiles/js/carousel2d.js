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

// Prueva contador
$(document).ready(function() {
    let animated = false; // Variable para evitar animaciones múltiples
    function animateCounter(element, endValue) {
        $(element).prop('Counter', 0).animate({
            Counter: endValue
        }, {
            duration: 2000, // Duración de la animación
            easing: 'swing',
            step: function(now) {
                $(this).text(Math.ceil(now)); // Actualiza el texto
            }
        });
    }
    $(window).on('scroll', function() {
        // Verifica si la sección está en la vista
        const sectionTop = $('.container-fluid').offset().top;
        const sectionBottom = sectionTop + $('.container-fluid').outerHeight();
        const scrollTop = $(this).scrollTop();
        const windowHeight = $(this).height();
        if (!animated && scrollTop + windowHeight >= sectionTop && scrollTop < sectionBottom) {
            animated = true; // Evita que se vuelva a animar
            animateCounter('.counter-profesionales', 14);
            animateCounter('.counter-clientes', 99);
        }
    });
});