from django.urls import path
from . import views
from .views import EmergenciaDetailAPIView, EmergenciaListCreateAPIView, EvidenciaDetailAPIView, EvidenciaListCreateAPIView, FaunaFloraDetailAPIView, FaunaFloraListCreateAPIView, ImagenDetailAPIView, ImagenListCreateAPIView, RolDetailAPIView, RolListCreateAPIView, UbicacionDetailAPIView, UbicacionListCreateAPIView, UsuarioDetailAPIView, UsuarioListCreateAPIView, ZonaDetailAPIView, ZonaListCreateAPIView


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

    #Ubicacion
    path('api/models/ubicacion', UbicacionListCreateAPIView.as_view(), name='listar_crear_ubicacion'), 
    path('api/models/ubicacion/<int:pk>/', UbicacionDetailAPIView.as_view(), name='ubicacion-detail'), 

    #Evidencia
    path('api/models/evidencia', EvidenciaListCreateAPIView.as_view(), name='listar_crear_evidencia'), 
    path('api/models/evidencia/<int:pk>/', EvidenciaDetailAPIView.as_view(), name='evidencia-detail'),

    #Fauna y flora
    path('api/models/faunaflora', FaunaFloraListCreateAPIView.as_view(), name='listar_crear_faunaflora'), 
    path('api/models/faunaflora/<int:pk>/', FaunaFloraDetailAPIView.as_view(), name='faunaflora-detail'),
     
     #Imagen
    path('api/models/imagen', ImagenListCreateAPIView.as_view(), name='listar_crear_imagen'), 
    path('api/models/imagen/<int:pk>/', ImagenDetailAPIView.as_view(), name='iamgen-detail'),

    #Emergencia
    path('api/models/emergencia', EmergenciaListCreateAPIView.as_view(), name='listar_crear_emergencia'), 
    path('api/models/emergencia/<int:pk>/', EmergenciaDetailAPIView.as_view(), name='emergencia-detail'),

]
