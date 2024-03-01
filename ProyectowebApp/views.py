from django.shortcuts import render,HttpResponse

#from servicios.models import Servicio

# Create your views here.

def home(request):
    return render(request,"ProyectowebApp/home.html")

def tienda(request):
    return render(request,"ProyectowebApp/tienda.html")

def contacto(request):
    return render(request,"ProyectowebApp/contacto.html")
