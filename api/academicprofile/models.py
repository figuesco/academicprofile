from django.db import models

# Create your models here.
from users.models import User
from tkinter import CASCADE
from django.conf import settings

class academicprofile(models.Model):

    EDUCATION_LEVEL = (
        (1, 'Carrera tecnica'),
        (2, 'Universidad'),
        (3, 'Maestría'),
        (4, 'Doctorado'),
        (5, 'Curso'),
        (6, 'Certificación')
    )

    STATUS_ACADEMIC = (
        (1, 'Finalizado'),
        (2, 'Incompleto'),
        (3, 'En curso')
    )

    name = models.CharField(max_length=32)
    institution = models.CharField(max_length=32)
    duration = models.CharField(max_length=32)

    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL)

    status_academic = models.CharField(max_length=20, choices=STATUS_ACADEMIC)

    user = models.OneToOneField(User, on_delete= models.CASCADE)

    def  __str__(self):
        return self.User.user_id
