from django.contrib import admin

from .models import Professor


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = [
        'user__first_name', 'user__last_name', 'formacao',
        'nivel', 'estado',
    ]
    list_display_links = [
        'user__first_name', 'user__last_name'
    ]
    list_filter = [
        'formacao', 'estado', 'nivel'
    ]
