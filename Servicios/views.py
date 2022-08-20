from django.shortcuts import render
from Servicios.models import Servicio

# Create your views here.
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'ProyectoWebApp/servicios.html', {'servicios':servicios})
