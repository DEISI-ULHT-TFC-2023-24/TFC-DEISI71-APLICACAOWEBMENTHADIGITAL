# Generated by Django 4.2.6 on 2024-02-04 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0003_remove_mentor_grupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='funcao',
            field=models.CharField(default='', max_length=20),
        ),
    ]
