# Generated by Django 4.2.6 on 2024-02-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0025_alter_risk_pre_diabetico'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='pergunta_cardiovascular',
            field=models.CharField(choices=[('Baixo', 'Baixo'), ('Moderado', 'Moderado'), ('Alto', 'Alto'), ('Elevado', 'Elevado')], default='Alto', max_length=10),
        ),
    ]