from django.db import models

from users.models import BaseModel, User


class Professor(BaseModel):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Usuário',
        related_name='professor'
    )
    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento',
        auto_created=False
    )
    formacao = models.CharField(
        verbose_name='Formação',
        max_length=255,
        blank=False,
        null=True
    )
    nivel = models.CharField(
        verbose_name='Nível',
        max_length=50,
        blank=False,
        null=True,
        choices=(
            ('Graduação', 'Graduação'),
            ('Pós-Graduação', 'Pós-Graduação'),
            ('Mestrado', 'Mestrado'),
            ('Doutorado', 'Doutorado'),
        ),
        default='Graduação'
    )
    estado = models.CharField(
        verbose_name='Estado',
        max_length=2,
        blank=False,
        null=True
    )

    def __str__(self) -> str:
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
        ordering = ['created_at', ]
