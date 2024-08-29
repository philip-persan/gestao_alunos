from django import forms

from .models import Turma


class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        excludes = ['created_at', 'updated_at']
