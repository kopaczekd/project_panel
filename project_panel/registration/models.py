from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserDashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.ForeignKey(Role, null=True, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nazwa firmy")
    nip = models.CharField(null=True, blank=True, verbose_name="Nip firmy", max_length=248)
    postal_address = models.CharField(max_length=255, verbose_name="Adres pocztowy")
    telephone = models.PositiveIntegerField(verbose_name="Nr telefonu")
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, {self.telephone}'

    def is_executive(self):
        role = Role.objects.filter(name='Wykonawca').first()
        if self.role == role:
            return True
        else:
            return False

    @classmethod
    def get_all_executors(cls):
        return UserDashboard.objects.filter(role__id=1).only('user')
