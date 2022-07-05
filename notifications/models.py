from django.db import models

# Create your models here.
from users.models import User
from tkinter import CASCADE
from django.conf import settings

class notification(models.Model):

    message =