from django.contrib import admin

from .models import Horario


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = [
        'turma', 'disciplina', 'dia_semana',
        'hora_inicio', 'hora_fim'
    ]
    list_display_links = [
        'turma', 'disciplina'
    ]
    list_filter = [
        'turma', 'disciplina', 'dia_semana'
    ]
