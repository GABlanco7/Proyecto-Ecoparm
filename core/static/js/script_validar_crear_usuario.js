document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registroForm");

    const campos = {
        nombre: document.getElementById("nombre"),
        apellido: document.getElementById("apellido"),
        identificacion: document.getElementById("identificacion"),
        genero: document.getElementById("genero"),
        email: document.getElementById("email"),
        telefono: document.getElementById("telefono"),
        password: document.getElementById("password"),
        confirmPassword: document.getElementById("confirmPassword"),
        errorMensaje: document.getElementById("error-message"),
        mensaje: document.getElementById("mensaje")
    };

    // Función para mostrar toast
    function mostrarToast(mensaje, tipo = "error") {
        const toast = document.getElementById("toast");
        toast.className = "toast";
        toast.textContent = mensaje;

        if (tipo === "success") toast.classList.add("success");
        else if (tipo === "info") toast.classList.add("info");
        else if (tipo === "warning") toast.classList.add("warning");

        toast.classList.add("show");

        setTimeout(() => {
            toast.classList.remove("show");
        }, 3000);
    }

    // Limitar entrada a números
    campos.identificacion.addEventListener("input", function () {
        this.value = this.value.replace(/[^0-9]/g, '');
    });
    campos.telefono.addEventListener("input", function () {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    form.addEventListener("submit", function (e) {
        e.preventDefault(); // Evita que se envíe el formulario directamente

        // Limpiar errores anteriores
        campos.errorMensaje.textContent = "";
        campos.mensaje.textContent = "";

        const valores = {
            nombre: campos.nombre.value.trim(),
            apellido: campos.apellido.value.trim(),
            identificacion: campos.identificacion.value.trim(),
            genero: campos.genero.value.trim(),
            email: campos.email.value.trim(),
            telefono: campos.telefono.value.trim(),
            password: campos.password.value,
            confirmPassword: campos.confirmPassword.value
        };

        // Verificar campos vacíos
        for (const [key, val] of Object.entries(valores)) {
            if (!val && key !== 'confirmPassword') {
                mostrarToast(`El campo ${key} no puede estar vacío.`, "warning");
                campos[key].focus();
                return;
            }
        }

        // Validación numérica
        if (!/^\d+$/.test(valores.identificacion)) {
            mostrarToast("La identificación solo debe contener números.", "error");
            campos.identificacion.focus();
            return;
        }

        if (!/^\d+$/.test(valores.telefono)) {
            mostrarToast("El teléfono solo debe contener números.", "error");
            campos.telefono.focus();
            return;
        }

        // Validar correo electrónico
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(valores.email)) {
            mostrarToast("El correo electrónico no es válido.", "error");
            campos.email.focus();
            return;
        }

        // Validación de contraseña
        const errores = [];
        if (valores.password.length < 8) errores.push("al menos 8 caracteres");
        if (!/[A-Z]/.test(valores.password)) errores.push("una letra mayúscula");
        if (!/[a-z]/.test(valores.password)) errores.push("una letra minúscula");
        if (!/[0-9]/.test(valores.password)) errores.push("un número");
        if (!/[^A-Za-z0-9]/.test(valores.password)) errores.push("un carácter especial");

        if (errores.length > 0) {
            mostrarToast("La contraseña debe contener: " + errores.join(", "), "warning");
            campos.password.focus();
            return;
        }

        // Confirmar contraseñas
        if (valores.password !== valores.confirmPassword) {
            mostrarToast("Las contraseñas no coinciden.", "error");
            campos.confirmPassword.focus();
            return;
        }

        // Si todo está bien
        mostrarToast("¡Usuario registrado con éxito!", "success");
        campos.mensaje.style.color = "green";
        campos.mensaje.textContent = "¡Usuario registrado con éxito!";
        // form.submit(); // Descomenta si deseas enviar el formulario
    });
});
