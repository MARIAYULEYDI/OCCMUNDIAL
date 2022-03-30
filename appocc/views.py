from django.shortcuts import render
from.models import Noticias, Comentarios
from.forms import ComentariosForm
# Create your views here.   
        
def index(request):
    return render(request, 'app/index.html')
def events(request):
    # soli = solicitud.objects.all()
    # datos = {
    #     "soli" : soli
    #     }
    return render(request, 'app/events.html')
def elements(request):
    Notis = Noticias.objects.all()
    datos = {
        "Notis" : Notis
        }
    return render(request, 'app/elements.html', datos)
def events_news(request):
    return render(request, 'app/events_news.html')
def single_event(request):
    return render(request, 'app/single_events.html')
def contact(request):
    datos =  {
        "form": ComentariosForm
    }
    if request.method == 'POST':
        formulario = ComentariosForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos["form"] = formulario
    return render(request, 'app/contact.html', datos)

def Registro(request):
    return render(request, 'app/Registro.html')

def buscar(request): 
    if request.GET ['busqueda']:
        query = request.GET['busqueda']
        Notis = Noticias.objects.filter(titulo=query).order_by('-informacion')
        datos ={
            "Noticias" : Noticias,
            "query": query
        }
        return render(request, 'app/registro_b.html', datos)
    else:
        return render (request, 'app/registro_b.html')
