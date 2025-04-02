from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def admin_page(request):
    return render(request, 'core/admin.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def guardaparamo(request):
    return render(request, 'core/guardaparamo.html')

def login_page(request):
    return render(request, 'core/login.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def recuperar_contraseña(request):
    return render(request, 'core/recuperar_contrasena.html')


def login_page(request):
    if request.method == 'POST':
        # Obtención de los datos del formulario
        username = request.POST.get('usuario')  # Es recomendable usar get() para evitar KeyError
        password = request.POST.get('password')
        tipo_usuario = request.POST.get('tipo-usuario')

        if not username or not password or not tipo_usuario:
            messages.error(request, "Por favor, ingrese todos los campos.")
            return render(request, 'core/login.html')

        # Intentar obtener el usuario
        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            user_obj = None

        # Si el usuario existe y las credenciales son correctas
        if user_obj:
            user = authenticate(request, username=user_obj.username, password=password)
            if user is not None:
                # Si la autenticación es exitosa, iniciamos sesión
                login(request, user)

                # Redirección dependiendo del tipo de usuario
                if user.is_superuser:
                    return redirect('admin')  # Redirige al área de administración si es superusuario
                elif tipo_usuario == "guardaparamo":
                    return redirect('guardaparamo')  # Redirige a la vista del guardaparamo
                else:
                    messages.error(request, "Tipo de usuario no válido.")
                    return render(request, 'core/login.html')
            else:
                messages.error(request, "Credenciales incorrectas.")
        else:
            messages.error(request, "El usuario no existe.")

    return render(request, 'core/login.html')