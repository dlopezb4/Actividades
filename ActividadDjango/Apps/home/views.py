from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import Administradores, Estudiante
from .forms import EstudianteForms,AdministradorForms
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name='index.html'

class CreditosView(TemplateView):
    template_name='creditos.html'

class EstudiantesView(TemplateView):
    template_name='estudiantes.html'

class AdministradoresView(TemplateView):
    template_name='Administradores.html'

class AcercadeView(TemplateView):
    template_name='acercade.html'

class ContactoView(TemplateView):
    template_name='contacto.html'

class ListarEstudiante(ListView):
    template_name = 'listar_est.html'
    model = Estudiante 

    def get_queryset(self):
        return Estudiante.objects.all()

class ListarAdministradores(ListView):
    template_name='administradores.html'
    model = Administradores

class CrearEstudianteView(CreateView):
    template_name = 'crear_estudiante.html'
    form_class = EstudianteForms 
    success_url = reverse_lazy('home:crear')

class CrearAdminView(CreateView):
    template_name = 'crear_admin.html'
    form_class = AdministradorForms 
    success_url = reverse_lazy('home:Crear')