from django.core.exceptions import ValidationError
from django.db import models

from disciplina.models import Disciplina
from professor.models import Professor
from users.models import BaseModel


class Turma(BaseModel):
    professor = models.ForeignKey(
        verbose_name='Professor',
        to=Professor,
        on_delete=models.SET_NULL,
        help_text='Professor responável pela turma.',
        null=True,
        related_name='turmas'
    )
    nome = models.CharField(
        verbose_name='Nome',
        max_length=255,
        blank=False,
        null=True,
        help_text='Nome/Identificação da turma.'
    )
    ano = models.IntegerField(
        verbose_name='Ano',
        blank=False,
        help_text='Ano da turma Ex.: 2024'
    )

    def __str__(self) -> str:
        return f'{self.nome}/{self.ano}'

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
        ordering = ['ano', ]


class Aluno(BaseModel):
    nome_completo = models.CharField(
        verbose_name='Nome Completo',
        max_length=255,
        blank=False,
        null=True
    )
    data_nascimento = models.DateField(
        verbose_name='Data de nascimento',
        auto_created=False,
        blank=False,
        null=True
    )
    endereco = models.CharField(
        verbose_name='Endereço',
        max_length=255,
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name='E-mail',
        blank=True,
        null=True
    )
    telefone = models.CharField(
        verbose_name='Telefone do aluno',
        max_length=14,
        blank=True,
        null=True
    )
    turma = models.ForeignKey(
        verbose_name='Turma',
        to=Turma,
        on_delete=models.CASCADE,
        related_name='alunos'
    )

    def __str__(self) -> str:
        return f'{self.nome_completo} - {self.turma}'

    class Meta:
        verbose_name = 'Aluno(a)'
        verbose_name_plural = 'Alunos'
        ordering = ['turma', 'nome_completo']


class Nota(BaseModel):
    aluno = models.ForeignKey(
        verbose_name='Aluno(a)',
        to=Aluno,
        on_delete=models.CASCADE,
        related_name='notas'
    )
    turma = models.ForeignKey(
        verbose_name='Turma',
        to=Turma,
        on_delete=models.CASCADE,
        related_name='notas'
    )
    disciplina = models.ForeignKey(
        verbose_name='Disciplina',
        to=Disciplina,
        on_delete=models.SET_NULL,
        blank=False,
        null=True
    )
    valor_nota = models.FloatField(
        verbose_name='Valor da Nota',
    )
    data_lancamento = models.DateField(
        verbose_name='Data de lançamento',
        auto_now=False
    )

    def __str__(self) -> str:
        return f'{self.aluno} - {self.disciplina}'

    def clean(self) -> None:
        if self.valor_nota < 0 or self.valor_nota > 10:
            raise ValidationError('A nota deve estar entre 0 e 10.')

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        ordering = ['data_lancamento', 'aluno', 'disciplina']
