from django.shortcuts import render
from django.views.generic import ListView
from general.models import Registrado
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from general.forms import RegistradoForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.

def inicio(request):
    return render(request,'general/index.html')

def about_me(request):
    return render(request,'general/about_me.html')

def bandas(request):
    return render(request,'general/bandas.html')

def contacto(request):
    return render(request,'general/contacto.html')

#usuarios comunes pueden cargar datos para registarse al evento.

def register(request):
    
    if request.method == 'POST':

        
        register_form = RegistradoForm(request.POST,request.FILES)

        if register_form.is_valid():
            data = register_form.cleaned_data
            registro = Registrado(nombre=data["nombre"], apellido=data["apellido"],edad=data["edad"],localidad=data["localidad"],e_mail=data["e_mail"],cel=data["cel"],foto=data["foto"])
            registro.save()
            return render(request,'general/index.html')
        
    register_form = RegistradoForm()    


    return render(request,'general/register.html',{"form":register_form})


def sponsors(request):
    return render(request,'general/sponsors.html')

# vistas basadas en clases

class RegistradoList(ListView):
    model=Registrado
    template_name="general/lista_registrados.html"

class RegistradoDetalle(LoginRequiredMixin,DetailView):
    model=Registrado
    template_name="general/detalle_registrados.html"

class RegistradoBorrar(LoginRequiredMixin,DeleteView):
    model=Registrado
    template_name="general/borrar_registrados.html"
    success_url = "/general/lista_registrados"

class RegistradoUpdate(LoginRequiredMixin,UpdateView):
    model=Registrado
    template_name = 'general/editar_registrados.html'
    success_url = '/general/lista_registrados/'
    fields = ['nombre','apellido','edad','localidad','e_mail','cel','foto']

# login y logout

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "general/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "general/index.html", {"mensaje":"Datos incorrectos"})
            
        else:

            return render(request, "general/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "general/login.html", {'form': form})
