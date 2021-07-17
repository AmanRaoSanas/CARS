from django.contrib import admin
from import_export.admin import ImportExpirtModelAdmin

from .models import Info, Data


# Register your models here.
@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'password')


@admin.register(Data)
class DataAdmin(ImportExpirtModelAdmin):
    pass

# admin.site.register(Data,DataAdmin)