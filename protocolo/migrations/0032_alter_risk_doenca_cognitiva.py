# Generated by Django 4.2.6 on 2024-04-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0031_alter_risk_doenca_cognitiva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='doenca_cognitiva',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não'), ('Não se sabe', 'Não se sabe')], default='Não se sabe', max_length=100),
        ),
    ]