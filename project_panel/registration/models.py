from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserDashboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, null=True, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=248, null=True)
    nip = models.IntegerField(null=True)
    postal_address = models.CharField(max_length=248)
    telephone = models.PositiveIntegerField()
