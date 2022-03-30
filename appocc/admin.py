from django.contrib import admin
from .models import solicitud, Noticias, Inovaciones, Comentarios

class SeccionNoticiasAdmin(admin.ModelAdmin):
    list_display =[ "titulo", "imagen", "titulo_imagen", "informacion"]
    list_editable=["informacion"]
    search_fields = ["fecha_creacion"]
    list_filter =["fecha_creacion"]
    list_per_page = 10

class SeccionSolicitudAdmin(admin.ModelAdmin):
    list_display =[ "titulo", "empresa","", "imagen", "titulo_imagen", "informacion"]
    list_editable=["informacion"]
    search_fields = ["fecha_creacion"]
    list_filter =["fecha_creacion"]
    list_per_page = 10
# Register your models here.
admin.site.register(Noticias,SeccionNoticiasAdmin)
admin.site.register(solicitud)
admin.site.register(Inovaciones)
admin.site.register(Comentarios)