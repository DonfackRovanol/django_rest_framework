# Generated by Django 4.0.8 on 2023-04-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreprise',
            name='addresse',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='entreprise',
            name='nom',
            field=models.CharField(max_length=500),
        ),
    ]