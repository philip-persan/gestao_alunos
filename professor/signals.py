from django.db.models.signals import post_save
from django.dispatch import receiver

from professor.models import Professor
from users.models import User


@receiver(post_save, sender=User)
def create_professor(sender, instance, created, **kwargs):
    if created:
        # Cria um Professor automaticamente quando um novo User é criado
        Professor.objects.create(user=instance)
