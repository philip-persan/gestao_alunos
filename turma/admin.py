from django.contrib import admin

from .models import Aluno, Nota, Turma


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = [
        'professor', 'nome', 'ano'
    ]
    list_display_links = [
        'professor', 'nome'
    ]
    list_filter = [
        'professor',
    ]


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'email', 'telefone', 'turma'
    ]
    list_display_links = [
        'nome_completo', 'turma'
    ]
    list_filter = [
        'turma'
    ]


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = [
        'aluno', 'turma',
        'disciplina', 'valor_nota'
    ]
    list_display_links = [
        'aluno', 'turma'
    ]
    list_filter = [
        'turma', 'disciplina'
    ]
