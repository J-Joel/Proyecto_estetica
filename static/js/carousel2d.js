(function ($) {
    "use strict";

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    $('#product-carousel').owlCarousel({
        autoplay: false,
        autoplayHoverPause: true, // Pausa al pasar el ratón por encima
        smartSpeed: 1500,
        center: true,
        margin: 8, /* Reducir el margen entre elementos */
        dots: false,
        loop: true, // Permitir bucle
        nav: true, // Habilita las flechas de navegación
        navText: [
            '<i class="fa fa-angle-left" aria-hidden="true"></i>',
            '<i class="fa fa-angle-right" aria-hidden="true"></i>'
        ], // Personaliza las flechas
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });
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
            animateCounter('.counter-profesionales', 6);
            animateCounter('.counter-clientes', 100);
        }
    });
})(jQuery);