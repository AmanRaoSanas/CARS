# Generated by Django 3.1.7 on 2021-04-09 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='first_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='info',
            name='last_name',
            field=models.CharField(max_length=120),
        ),
    ]
