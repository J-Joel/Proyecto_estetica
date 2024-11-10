
        // Intercepta el envío del formulario anterio 
        document.getElementById("contactForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Evita el envío tradicional
        const form = event.target;
        
        // Enviar el formulario usando fetch Talia
        fetch(form.action, {
            method: 'POST',
            body: new FormData(form),
            })
        .then(response => {
            // Si la respuesta es exitosa, mostrar el popup de confirmación
            if (response.ok) {
                Swal.fire({
                    title: '¡Mensaje Enviado!',
                    text: 'Gracias por contactarnos. Tu mensaje ha sido enviado correctamente.',
                    icon: 'success',
                    confirmButtonText: 'volver',
                    confirmButtonColor: '#ff69b4' // Color rosa para el botón 
                }).then(() => {
                    window.location.href = '#contactForm'; // Regresa a la sección de contactos
                });
                    } else {
                    throw new Error('Error al enviar el formulario');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    Swal.fire({
                        title: 'Error',
                        text: 'Hubo un problema al enviar el mensaje. Por favor, inténtalo de nuevo más tarde.',
                        icon: 'error',
                        confirmButtonText: 'Cerrar'//Tengo que revisar que se envio el correo
                    });
                });
            });
    
        