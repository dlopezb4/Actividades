"""HOME Actividad2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from Apps.home.views import HomeView
from django.contrib import admin
from django.urls import path
from .views import HomeView,CreditosView,EstudiantesView,AdministradoresView,AcercadeView,ContactoView
from .views import ListarEstudiante, CrearEstudianteView,CrearAdminView
app_name = 'home'

urlpatterns = [
    path('index/', HomeView.as_view(), name='home'),
    path('creditos/', CreditosView.as_view(), name='creditos'),
    path('estudiantes/', EstudiantesView.as_view(), name='estudiantes'),
    path('administradores/', AdministradoresView.as_view(), name='administradores'),
    path('acercade/', AcercadeView.as_view(), name='acercade'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('listest/', ListarEstudiante.as_view(), name='listar_est'),
    path('crear/', CrearEstudianteView.as_view(), name='crear'),
    path('crear_admin/', CrearAdminView.as_view(), name='Crear'),
]