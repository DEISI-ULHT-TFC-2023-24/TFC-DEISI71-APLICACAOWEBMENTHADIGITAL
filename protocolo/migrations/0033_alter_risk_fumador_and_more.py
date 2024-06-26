# Generated by Django 4.2.6 on 2024-04-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0032_alter_risk_doenca_cognitiva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='fumador',
            field=models.CharField(choices=[('smoking', 'smoking'), ('nonSmoking', 'nonSmoking'), ('exSmoker', 'exSmoker'), ('naoSeSabe', 'naoSeSabe')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='risk',
            name='pergunta_cardiovascular',
            field=models.CharField(choices=[('Baixo', 'Baixo'), ('Moderado', 'Moderado'), ('Alto', 'Alto'), ('Elevado', 'Elevado'), ('Não se sabe', 'Não se sabe')], default='Não se sabe', max_length=100),
        ),
    ]
