from django.contrib import admin
# Register your models here.
# default: "Administração do Django"
from django.utils.timezone import now

admin.site.site_header = 'Painel de Controle'

# defaut: " Administração do Site"
admin.site.index_title = 'Recursos'

# default: "Site de Administração do Django"
admin.site.site_title = 'Título do HTML do Site'
from .models import Tema, ItemTema, Cliente, Endereco, Aluguel

class AdminTema(admin.ModelAdmin):
    list_display = ('nome', 'cor_toalha')

class AdminAluguel(admin.ModelAdmin):
    list_display = ('cliente','data_festa','hora_inicio','hora_termino', 'tema', 'endereco')
    list_filter = ('data_festa', 'endereco','tema', 'cliente')

class AdminCliente(admin.ModelAdmin):
    list_display = ('nome', 'telefone')

class AdminItemTema(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'tema')
    list_filter = ('tema', 'nome')

class AdminEndereco(admin.ModelAdmin):
    list_display = ('logradouro', 'numero','bairro','cidade', 'uf', 'cep')
    list_filter = ('bairro', 'uf', 'cidade')

admin.site.register(Tema, AdminTema)
admin.site.register(Cliente, AdminCliente)
admin.site.register(ItemTema, AdminItemTema)
admin.site.register(Endereco, AdminEndereco)
admin.site.register(Aluguel, AdminAluguel)

