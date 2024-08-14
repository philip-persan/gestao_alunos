from django.db import models

from users.models import BaseModel


class Disciplina(BaseModel):
    nome = models.CharField(
        verbose_name='Nome da Disciplina',
        max_length=255,
        blank=False
    )
    descricao = models.TextField(
        verbose_name='Descrição',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['nome']
