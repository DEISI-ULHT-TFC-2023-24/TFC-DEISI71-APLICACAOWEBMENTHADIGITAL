# Generated by Django 4.2.6 on 2024-03-15 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0014_alter_cuidador_escolhamultiplateste_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuidador',
            old_name='escolhaMultiplaTeste',
            new_name='diagnosticoPrincipal',
        ),
        migrations.RenameField(
            model_name='participante',
            old_name='escolhaMultiplaTeste',
            new_name='diagnosticoPrincipal',
        ),
    ]
