# Generated by Django 4.2.6 on 2024-02-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0014_risk_ifcc_risk_ngsp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='recomendacoes',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
