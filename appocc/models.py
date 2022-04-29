from django.db import models
import datetime

# Create your models here.
  
class solicitud (models.Model):
      solicitud_empleo = models.CharField(max_length=100, blank=False, null=False)
      ciudad_residencia = models.CharField(max_length=100, blank=False, null=False)
      horarios_disponibles = models.DateField(default=datetime.date.today, blank=False, null=False)
      informacion_curricular =  models.TextField(blank=False, null=True)
      edad = models.CharField(max_length=5, blank=False, null=False)
      fecha_solicitud = models.DateField(default=datetime.date.today, blank=False, null=False)
      años_experiencia = models.CharField(max_length=2, blank=False, null=False)
      email = models.EmailField(blank=False, null=True)
      telefono = models.CharField(max_length=12, blank=False, null=True)
      imagen_personal = models.ImageField(null=True, upload_to='solicitudes')
      titulo_imagen = models.CharField(max_length=100, blank=False, null=False)
      #empresa = models.CharField(max_length=100, blank=False, null=False)
      #empleo_solicitado = models.CharField(max_length=100, blank=False, null=False)
      #requisitos = models.TextField(blank=False, null=False)
      #sueldo = models.FloatField(blank=False, null=False)
      #disponible = models.BooleanField(default=True) para hacer selecciones
      #cantidad = models.IntegerField(null=Flase, default=100) Cantidad que se agrega
      #enlace_formulario = models.URLField(blank=False, null=False)
      #video = models.FileField(upload_to="Videos") Para videos

      def __str__(self):
          return self.email

class Noticias (models.Model):
      titulo = models.CharField(max_length=100, blank=False, null=False)
      #empresa = models.CharField(max_length=100, blank=False, null=False)
      #ciudad = models.CharField(max_length=100, blank=False, null=False)
      #empleo_solicitado = models.CharField(max_length=100, blank=False, null=False)
      #requisitos = models.TextField(blank=False, null=False)
      imagen = models.ImageField(null=False, upload_to='noticias')
      titulo_imagen = models.CharField(max_length=100, blank=False, null=False)
      #sueldo = models.FloatField(blank=False, null=False)
      #horarios = models.DateField(default=datetime.date.today, blank=False, null=False)
      informacion =  models.TextField(blank=False, null=False)
      fecha_creacion = models.DateField(default=datetime.date.today, blank=False, null=False)
      #email = models.EmailField(blank=False, null=Flase) para correo electronico
      #disponible = models.BooleanField(default=True) para hacer selecciones
      #cantidad = models.IntegerField(null=Flase, default=100) Cantidad que se agrega
      enlace_informacion = models.URLField(blank=False, null=False)
      #video = models.FileField(upload_to="Videos") Para videos

      def __str__(self):
          return self.titulo


class Inovaciones (models.Model):
      titulo_inovacion = models.CharField(max_length=100, blank=False, null=False)
      empresa = models.CharField(max_length=100, blank=False, null=False)
      #ciudad = models.CharField(max_length=100, blank=False, null=False)
      #empleo_solicitado = models.CharField(max_length=100, blank=False, null=False)
      #requisitos = models.TextField(blank=False, null=False)
      imagen = models.ImageField(null=True, upload_to='Inovaciones')
      titulo_imagen = models.CharField(max_length=100, blank=False, null=False)
      #sueldo = models.FloatField(blank=False, null=False)
      fecha = models.DateField(default=datetime.date.today, blank=False, null=False)
      informacion =  models.TextField(blank=False, null=False)
      fecha_creacion = models.DateField(default=datetime.date.today, blank=False, null=False)
      #email = models.EmailField(blank=False, null=Flase) para correo electronico
      #disponible = models.BooleanField(default=True) para hacer selecciones
      #cantidad = models.IntegerField(null=Flase, default=100) Cantidad que se agrega
      enlace_video = models.URLField(blank=False, null=False)
      #video = models.FileField(upload_to="Videos") Para videos

      def __str__(self):
          return self.titulo_inovacion

class Comentarios(models.Model):
    nombre = models.CharField(max_length=150, blank=False, null=False)
    email = models.CharField(max_length=150, blank=False, null=False)
    website = models.URLField(max_length=150, blank=False, null=True)
    comentarios = models.TextField(blank=False, null=False)


    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural =("Comments")

    def __str__(self):
        return self.nombre