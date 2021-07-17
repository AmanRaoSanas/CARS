# Generated by Django 3.1.7 on 2021-04-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('first_name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('last_name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('email', models.EmailField(max_length=120, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
    ]
