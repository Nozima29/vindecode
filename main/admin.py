from django.contrib import admin
from .models import *
# Register your models here.


class VINDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'vincode', 'model', 'year', 'make']


admin.site.register(VINData, VINDataAdmin)
