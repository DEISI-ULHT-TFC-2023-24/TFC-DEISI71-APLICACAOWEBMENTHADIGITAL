# Generated by Django 4.2.5 on 2024-02-26 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0018_alter_risk_ngsp_hba1'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='pergunta_cardiovascular',
            field=models.CharField(choices=[('Baixo', 'Sim'), ('Moderado', 'Moderado'), ('Alto', 'Alto'), ('Elevado', 'Elevado')], default='Baixo', max_length=20),
        ),
    ]
