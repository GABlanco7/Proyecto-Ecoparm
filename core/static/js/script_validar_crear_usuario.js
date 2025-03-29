function validarFormulario() {
    // Obtener los valores de los campos del formulario
    const nombre = document.getElementById("nombre").value;
    const apellido = document.getElementById("apellido").value;
    const identificacion = document.getElementById("identificacion").value;
    const genero = document.getElementById("genero").value;
    const email = document.getElementById("email").value;
    const telefono = document.getElementById("telefono").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Verificar que todos los campos estén llenos
    if (!nombre || !apellido || !identificacion || !genero || !email || !telefono || !password || !confirmPassword) {
        alert("Todos los campos deben estar llenos.");
        return false; // Evita que el formulario se envíe
    }

    // Validación de correo electrónico (básica)
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
        alert("Por favor, ingresa un correo electrónico válido.");
        return false;
    }

    // Verificar que las contraseñas coincidan
    if (password !== confirmPassword) {
        alert("Las contraseñas no coinciden.");
        return false; // Evita que el formulario se envíe
    }

    // Si todo es correcto, mostrar un mensaje de éxito
    alert("Formulario validado correctamente. ¡Gracias por registrarte!");
    
    // Si todo es correcto, permitir el envío
    return true;
}
