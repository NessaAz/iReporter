from re import A
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Admin)
admin.site.register(models.Client)
