from django.contrib import admin
from .models import Militar, Permiso, Licencias

# Register your models here.
admin.site.register(Permiso)
admin.site.register(Militar)
admin.site.register(Licencias)
