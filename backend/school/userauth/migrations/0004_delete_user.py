# Generated by Django 4.0.8 on 2023-04-11 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_alter_entreprise_addresse_alter_entreprise_nom'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
