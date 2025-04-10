from django.urls import path
from . import views
from .views import RolDetailAPIView, RolListCreateAPIView, UsuarioDetailAPIView, UsuarioListCreateAPIView, ZonaDetailAPIView, ZonaListCreateAPIView


urlpatterns = [
    path('', views.index, name='index'),
    path('administrador/', views.admin_page, name='administrador'),
    path('galeria/', views.galeria, name='galeria'),
    path('guardaparamo/', views.guardaparamo, name='guardaparamo'),
    path('login/', views.login_page, name='login'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('recuperar_contraseña/', views.recuperar_contraseña, name='recuperar_contraseña'),

# 👇 Rutas API
    #Rol
    path('api/models/rol', RolListCreateAPIView.as_view(), name='listar_crear_roles'), #CREAR y MOSTRAR
    path('api/models/rol/<int:pk>/', RolDetailAPIView.as_view(), name='rol-detail'),  # Vista para PUT, LEER y DELETE
    
    #Zona
    path('api/models/zona', ZonaListCreateAPIView.as_view(), name='listar_crear_zona'), 
    path('api/models/zona/<int:pk>/', ZonaDetailAPIView.as_view(), name='zona-detail'), 
    
    #Usuario
    path('api/models/usuario', UsuarioListCreateAPIView.as_view(), name='listar_crear_usuario'), 
    path('api/models/usuario/<int:pk>/', UsuarioDetailAPIView.as_view(), name='usuario-detail'), 
]