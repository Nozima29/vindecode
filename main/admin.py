from django.contrib import admin
from .models import *
# Register your models here.


class VINDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(VINData, VINDataAdmin)
