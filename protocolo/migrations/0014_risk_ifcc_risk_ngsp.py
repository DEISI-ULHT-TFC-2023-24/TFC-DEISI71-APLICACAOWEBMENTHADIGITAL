# Generated by Django 4.2.6 on 2024-01-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0013_risk_eag'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk',
            name='ifcc',
            field=models.FloatField(default=20.0),
        ),
        migrations.AddField(
            model_name='risk',
            name='ngsp',
            field=models.IntegerField(default=4),
        ),
    ]
