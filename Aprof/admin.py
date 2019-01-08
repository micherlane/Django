
from django.contrib import admin
from .models import Turma, Professor

class AdminTurma(admin.TabularInline):
    model = Turma
    extra = 1

class AdminProfessor(admin.ModelAdmin):
    inlines = [AdminTurma]

admin.site.register(Turma)
admin.site.register(Professor,AdminProfessor)