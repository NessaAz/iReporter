from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from cloudinary.models import CloudinaryField


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
    fullname = models.CharField(max_length=80, blank=True, null=True)
    organisation = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=254, blank=True, null=True)
    profile_pic = CloudinaryField(default='https://res.cloudinary.com/dpww3jwgm/image/upload/v1654722449/default.png')
    location = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    fullname = models.CharField(max_length=80, blank=True, null=True)
    organisation = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(max_length=254, blank=True, null=True)
    profile_pic = CloudinaryField(default='https://res.cloudinary.com/dpww3jwgm/image/upload/v1654722449/default.png')
    location = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)


# Create your models here.
class RedFlag(models.Model):
    image = CloudinaryField(blank=True, null=True,
                            default='https://res.cloudinary.com/ireporter2022/image/upload/v1656953718/crime5_r8mbnm.jpg')
    title = models.CharField(max_length=250, blank=True)
    info = models.CharField(max_length=1050, blank=True)
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='flags', null=True, blank=True)
    location = models.TextField(blank=True)
    status = (
        ('investigation', 'investigation'),
        ('rejected', 'rejected'),
        ('resolved', 'resolved'),
    )
    stages = models.CharField(max_length=20, choices=status, default='', null=True)
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
    image = CloudinaryField(blank=True, null=True,
    default='https://res.cloudinary.com/ireporter2022/image/upload/v1656953718/crime5_r8mbnm.jpg')
    title = models.CharField(max_length=250, blank=True)
    info = models.CharField(max_length=1050, blank=True)
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='interventions', null=True, blank=True)
    status = (
        ('investigation', 'investigation'),
        ('rejected', 'rejected'),
        ('resolved', 'resolved'),
    )
    stages = models.CharField(max_length=20, choices=status, default='', null=True)
    location = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.title} intervention'

    class Meta:
        ordering = ["-pk"]

    def save_intervention(self):
        self.save()

    def delete_intervention(self):
        self.delete()
