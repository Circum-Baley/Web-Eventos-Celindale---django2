from django.contrib import admin
from .models import *


# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')


admin.site.register(Menu, MenuAdmin)
