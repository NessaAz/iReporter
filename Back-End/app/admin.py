from re import A
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Admin)
admin.site.register(models.Client)
admin.site.register(models.User)

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(RedFlag),
admin.site.register(Intervention),
admin.site.register(Status)
