from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class User(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Admin(models.Model):
    user = models.OneToOneField(User, related_name='admin', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')

    def __str__(self):
        return str(self.user.username)


# Create your models here.
class RedFlag(models.Model):
    image = CloudinaryField()
    title = models.CharField(max_length=250, blank=True)
    info = models.CharField(max_length=1050, blank=True)
    user = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='flags')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title} Red-flag'

    class Meta:
        ordering = ["-pk"]

    def save_flag(self):
        self.save()

    def delete_flag(self):
        self.delete()


class Intervention(models.Model):
    image = CloudinaryField()
    title = models.CharField(max_length=250, blank=True)
    info = models.CharField(max_length=1050, blank=True)
    user = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='interventions')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title} intervention'

    class Meta:
        ordering = ["-pk"]

    def save_intervention(self):
        self.save()

    def delete_intervention(self):
        self.delete()


class Status(models.Model):
    status = (
        ('investigation', 'investigation'),
        ('rejected', 'rejected'),
        ('resolved', 'resolved'),
    )
