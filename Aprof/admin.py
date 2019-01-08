
from django.contrib import admin
# Register your models here.
# default: "Administração do Django"
from django.utils.timezone import now

admin.site.site_header = 'Painel de Controle'

# defaut: " Administração do Site"
admin.site.index_title = 'Recursos'

# default: "Site de Administração do Django"
admin.site.site_title = 'Título do HTML do Site'
from .models import Turma, Professor

class AdminTurma(admin.TabularInline):
    model = Turma
    extra = 1

class AdminProfessor(admin.ModelAdmin):
    inlines = [AdminTurma]

admin.site.register(Turma)
admin.site.register(Professor,AdminProfessor)
