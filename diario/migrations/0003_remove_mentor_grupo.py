# Generated by Django 4.2.6 on 2024-02-04 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0002_alter_informacaosensivel_telemovel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor',
            name='grupo',
        ),
    ]
