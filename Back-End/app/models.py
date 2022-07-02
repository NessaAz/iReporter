from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class RedFlag(models.Model):
    image = CloudinaryField()
    title = models.CharField(max_length=250, blank=True)
    info = models.CharField(max_length=1050, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='flags')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interventions')
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
