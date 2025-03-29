function validateUserType(event) {
    event.preventDefault(); // Evitar el envío del formulario

    var tipoUsuario = document.getElementById('tipo-usuario')?.value;

    if (!tipoUsuario) {
        alert("Por favor, seleccione un tipo de usuario.");
        return;
    }

    // Guardar sesión en sessionStorage
    sessionStorage.setItem('isLoggedIn', 'true');
    sessionStorage.setItem('userType', tipoUsuario);

    // Redirigir según el tipo de usuario
    if (tipoUsuario === "administrador") {
        window.location.href = "/admin/";  // URL correcta en Django
    } else if (tipoUsuario === "guardaparamo") {
        window.location.href = "/guardaparamo/";  // URL correcta en Django
    } else {
        alert("Tipo de usuario no válido.");
    }
}

// Agregar el evento al formulario si existe
document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', validateUserType);
    }
});
