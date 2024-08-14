import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    id = models.UUIDField(
        verbose_name='id',
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    email = models.EmailField(
        verbose_name='email',
        unique=True,
        blank=False,
        null=False
    )
    telefone = models.CharField(
        max_length=20,
        verbose_name='telefone',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização'
    )

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['created_at', ]
