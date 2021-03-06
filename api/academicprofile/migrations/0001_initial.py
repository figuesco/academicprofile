# Generated by Django 4.0.3 on 2022-06-09 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='academicprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('institution', models.CharField(max_length=32)),
                ('duration', models.CharField(max_length=32)),
                ('education_level', models.CharField(choices=[(1, 'Carrera tecnica'), (2, 'Universidad'), (3, 'Maestría'), (4, 'Doctorado'), (5, 'Curso'), (6, 'Certificación')], max_length=20)),
                ('status_academic', models.CharField(choices=[(1, 'Finalizado'), (2, 'Incompleto'), (3, 'En curso')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
