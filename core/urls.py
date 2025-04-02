from django.urls import path
from .views import index, admin_page, galeria, guardaparamo, login_page, nosotros, recuperar_contraseña
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('admin_page/', admin_page, name='admin_page'),
    path('galeria/', galeria, name='galeria'),
    path('guardaparamo/', guardaparamo, name='guardaparamo'),
    path('login/', login_page, name='login'),
    path('nosotros/', nosotros, name='nosotros'),
    path('recuperar_contraseña/', recuperar_contraseña, name='recuperar_contraseña'),
    path('logout/', LogoutView.as_view(next_page='login_page'), name='logout'),
]