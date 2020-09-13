from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserDashboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, null=True, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=248, null=True, verbose_name="Nazwa firmy")
    nip = models.CharField(null=True, verbose_name="Nip firmy", max_length=248)
    postal_address = models.CharField(max_length=248, verbose_name="Adres pocztowy")
    telephone = models.PositiveIntegerField(verbose_name="Nr telefonu")

    def __str__(self):
        return f'{self.user}, {self.telephone}'

    def is_executive(self):
        role = Role.objects.filter(name='Wykonawca').first()
        if self.role == role:
            return True
        else:
            return False


