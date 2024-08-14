from django.db import models

from disciplina.models import Disciplina
from turma.models import Turma
from users.models import BaseModel


class Horario(BaseModel):
    turma = models.ForeignKey(
        verbose_name='Turma',
        to=Turma,
        on_delete=models.CASCADE,
        related_name='horarios'
    )
    disciplina = models.ForeignKey(
        verbose_name='Disciplina',
        to=Disciplina,
        on_delete=models.CASCADE,
        related_name='horarios'
    )
    dia_semana = models.CharField(
        verbose_name='Dia da semana',
        max_length=9,
        choices=[
            ('Segunda', 'Segunda'),
            ('Terça', 'Terça'),
            ('Quarta', 'Quarta'),
            ('Quinta', 'Quinta'),
            ('Sexta', 'Sexta'),
            ('Sábado', 'Sábado')
        ]
    )
    hora_inicio = models.TimeField(
        verbose_name='Hora de início'
    )
    hora_fim = models.TimeField(
        verbose_name='Hora de término'
    )

    def __str__(self):
        return f'{self.turma} - {self.disciplina} ({self.dia_semana})'

    class Meta:
        verbose_name = 'Horário'
        verbose_name_plural = 'Horários'
        ordering = ['dia_semana', 'hora_inicio']
