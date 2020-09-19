from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Tytuł projektu")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Klient")

    def __str__(self):
        return self.title
