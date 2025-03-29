window.onload = function() {
    setTimeout(function() {
        // Aquí cambiamos 'overlay_loader' a 'overlay'
        document.getElementById('overlay').style.display = 'none';
        
        // Aseguramos que el contenido principal se muestre una vez que el loader se oculta
        document.getElementById('content').style.display = 'block';
    }, 1000);  // El tiempo de espera en milisegundos (1000ms = 1 segundos)
}
