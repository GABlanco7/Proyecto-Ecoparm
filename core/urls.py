from django.urls import path
from . import views
from .views import RolListCreateAPIView, RolDetailAPIView


urlpatterns = [
    path('', views.index, name='index'),
    path('administrador/', views.admin_page, name='administrador'),
    path('galeria/', views.galeria, name='galeria'),
    path('guardaparamo/', views.guardaparamo, name='guardaparamo'),
    path('login/', views.login_page, name='login'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('recuperar_contraseña/', views.recuperar_contraseña, name='recuperar_contraseña'),

# 👇 Rutas API para Rol
    path('api/roles/', RolListCreateAPIView.as_view(), name='roles-list-create'),
    path('api/roles/<int:pk>/', RolDetailAPIView.as_view(), name='roles-detail'),

]