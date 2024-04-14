# Generated by Django 4.2.6 on 2024-03-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0010_cuidador_comorbilidades_participante_comorbilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuidador',
            name='escolhaMultiplaTeste',
            field=models.CharField(blank=True, choices=[('Alzheimer', 'Alzheimer'), ('Dor de cabeça aguda', 'Dor de cabeça aguda'), ('Dor de cabeça crónica', 'Dor de cabeça crónica'), ('Dor de cabeça recorrente', 'Dor de cabeça recorrente'), ('Dor de cabeça tensional', 'Dor de cabeça tensional'), ('Enxaqueca', 'Enxaqueca'), ('Epilepsia', 'Epilepsia'), ('Parkinson', 'Parkinson'), ('Outra', 'Outra')], default='Alzheimer', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='participante',
            name='escolhaMultiplaTeste',
            field=models.CharField(blank=True, choices=[('Alzheimer', 'Alzheimer'), ('Dor de cabeça aguda', 'Dor de cabeça aguda'), ('Dor de cabeça crónica', 'Dor de cabeça crónica'), ('Dor de cabeça recorrente', 'Dor de cabeça recorrente'), ('Dor de cabeça tensional', 'Dor de cabeça tensional'), ('Enxaqueca', 'Enxaqueca'), ('Epilepsia', 'Epilepsia'), ('Parkinson', 'Parkinson'), ('Outra', 'Outra')], default='Alzheimer', max_length=100, null=True),
        ),
    ]