from django.urls import path, include
from .views import index, events, elements, events_news, single_event, contact, Registro, buscar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='inicio'),
    path('events/', events, name='Eventos'),
    path('elements/', elements, name='Elementos'),
    path('events_news/', events_news, name='Eventos Nuevos'),
    path('single_event/', single_event, name='Siguiente Evento'),
    path('contact/', contact, name='Contacto'),
    path('Registro/', Registro, name='Registro'),
    path('buscar/', buscar, name='buscar'),

]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)