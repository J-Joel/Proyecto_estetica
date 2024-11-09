(function ($) {
    "use strict";
    
    // Smooth scrolling on the navbar links // Efecto de desplazamiento
    $(".navbar-nav a").on('click', function (event) {
        if (this.hash !== "") {
            event.preventDefault();
            
            $('html, body').animate({
                scrollTop: $(this.hash).offset().top - 45
            }, 1500, 'easeInOutExpo');
            
            if ($(this).parents('.navbar-nav').length) {
                $('.navbar-nav .active').removeClass('active');
                $(this).closest('a').addClass('active');
            }
        }
    }); 
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

    /* Script para que solo un menu este abierto */
    $('#userCollapse').on('show.bs.collapse', function () {
        $('#menuCollapse').collapse("hide");
    })
    $('#menuCollapse').on('show.bs.collapse', function () {
        $('#userCollapse').collapse("hide");
    })
    /*********************************************/
})(jQuery);