from django.urls import path, include
from .views import index, events, elements, events_news, single_event, contact, registro, buscar, CustomLoginView
from django.conf import settings
from django.conf.urls.static import static
from .forms import loginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='inicio'),
    path('events/', events, name='Eventos'),
    path('elements/', elements, name='Elementos'),
    path('events_news/', events_news, name='Eventos Nuevos'),
    path('single_event/', single_event, name='Evento'),
    path('contact/', contact, name='Contacto'),
    path('registro/', registro, name='registro'),
    path('buscar/', buscar, name='buscar'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='templates/app/login.html', authentication_form=loginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='templates/app/logout.html'), name='logout'),
]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)