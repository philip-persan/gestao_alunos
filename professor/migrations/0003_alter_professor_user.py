# Generated by Django 5.1 on 2024-08-14 17:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("professor", "0002_alter_professor_options_professor_nivel"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="professor",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="professor",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Usuário",
            ),
        ),
    ]
