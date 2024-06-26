# Generated by Django 4.2.5 on 2023-12-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0002_risk_doenca_cognitiva'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='pre_diabetico',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='risk',
            name='diabetes',
            field=models.BooleanField(default=True),
        ),
    ]
