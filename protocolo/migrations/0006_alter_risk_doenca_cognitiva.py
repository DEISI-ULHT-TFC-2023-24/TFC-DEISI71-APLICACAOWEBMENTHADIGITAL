# Generated by Django 4.2.6 on 2023-12-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0005_alter_risk_recomendacoesadicionais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='doenca_cognitiva',
            field=models.BooleanField(default=False),
        ),
    ]