# Generated by Django 4.2.6 on 2024-01-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0012_risk_recomendacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='eag',
            field=models.FloatField(default=68.0),
        ),
    ]