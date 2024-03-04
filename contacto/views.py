from django.shortcuts import render,redirect
from django.core.mail import EmailMessage

from . forms import FormularioContacto

# Create your views here.
def contacto(request):
    
    formulario_contacto=FormularioContacto()
    if request.method=="POST":
        #carga los datos enviados al pulsar el botón submit en el formulario en la variable
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde aplicación Gestión Pedidos",
                "Usuario {}, email: {} :\n{}".format(nombre,email,contenido),
                "",["manuelalonsoweb@gmail.com"], reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")  
            except:
                return redirect("/contacto/?novalido")                          

    return render(request,"contacto/contacto.html",{'miFormulario':formulario_contacto})