# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Marca, Modelo, Coche

# Register your models here.


admin.site.register(Marca)
admin.site.register(Modelo)

class CocheAdmin(admin.ModelAdmin):
        list_display = ('marca', 'modelo', 'fecha_creacion')
        list_filter = ('marca', 'modelo')
        #ordering = ('marca', 'modelo', 'fecha_creacion')
        class Meta:
            model = Coche
admin.site.register(Coche, CocheAdmin)
