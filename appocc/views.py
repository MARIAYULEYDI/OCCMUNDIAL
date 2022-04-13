from django.shortcuts import render, redirect 
from.models import Noticias, Comentarios
from.forms import ComentariosForm, userForm, loginForm 
from django.contrib import messages 
from django.views import View
from django.contrib.auth.views import LoginView

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

def registro(request):
    return render(request, 'app/registro.html')

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

class Registro(View):
    form_class = userForm
    initial = {'key': 'values'}
    template_name = ''

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect(to='/')
        return render(request, self.template_name, {'form': form})
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        return super(Registro, self).dispatch(request, *args, **kwargs)

class CustomLoginView(LoginView):
    form_class = loginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.sessio.modified = True
        return super(CustomLoginView, self).form_valid(form)        
