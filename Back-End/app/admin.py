from re import A
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Admin),
admin.site.register(Client),
admin.site.register(User),
admin.site.register(RedFlag),
admin.site.register(Intervention),
admin.site.register(Status)
