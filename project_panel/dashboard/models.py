from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name="Nazwa projektu")
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Klient", related_name="customer")
    executor = models.ManyToManyField(User, verbose_name="Wykonawca/y", related_name="executor")
    description = models.TextField(verbose_name="Opis projektu")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    status = models.ForeignKey(Status, default=1, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name= "Nazwa zadania")
    description = models.TextField(verbose_name="Opis zadania")
    spent_time = models.TimeField(verbose_name="Czas realizacji [h]")
    status = models.ForeignKey(Status, default=1, on_delete=models.DO_NOTHING)
    executor = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    price_per_hour = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title
