# Generated by Django 4.2.6 on 2024-04-03 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0028_alter_risk_pergunta_cardiovascular'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='risk',
            name='pre_diabetico',
        ),
    ]
