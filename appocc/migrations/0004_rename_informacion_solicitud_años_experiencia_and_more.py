# Generated by Django 4.0.1 on 2022-04-23 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appocc', '0003_comentarios_inovaciones_alter_noticias_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud',
            old_name='informacion',
            new_name='años_experiencia',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='ciudad',
            new_name='ciudad_residencia',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='requisitos',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='fecha_creacion',
            new_name='fecha_solicitud',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='horarios',
            new_name='horarios_disponibles',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='imagen',
            new_name='imagen_personal',
        ),
        migrations.RenameField(
            model_name='solicitud',
            old_name='empleo_solicitado',
            new_name='solicitud_empleo',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='enlace_formulario',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='sueldo',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='titulo',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='informacion_curricular',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='telefono',
            field=models.TextField(null=True),
        ),
    ]
