# Generated by Django 4.1.6 on 2023-02-07 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carro',
            old_name='concertos',
            new_name='consertos',
        ),
    ]
