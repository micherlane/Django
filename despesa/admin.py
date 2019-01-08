from django.contrib import admin
# Register your models here.
# default: "Administração do Django"
from django.utils.timezone import now

admin.site.site_header = 'Painel de Controle'

# defaut: " Administração do Site"
admin.site.index_title = 'Recursos'

# default: "Site de Administração do Django"
admin.site.site_title = 'Título do HTML do Site'
from .models import Despesa


class AdminDespesas(admin.ModelAdmin):
    list_display = ('data_criaçao', 'tipo_despesa', 'forma_pagamento', 'descriçao', 'vencimento', 'quitado','campo_temp')
    list_filter = ('quitado', 'vencimento')

admin.site.register(Despesa, AdminDespesas)
