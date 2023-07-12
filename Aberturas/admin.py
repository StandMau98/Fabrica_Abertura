from django.contrib import admin
from .models import *

class TrabajosAdmin(admin.ModelAdmin):
    readonly_fields = ("date", "modify")

admin.site.register(Trabajo_PVC,TrabajosAdmin)
admin.site.register(Trabajo_Aluminio,TrabajosAdmin)

# Register your models here.
