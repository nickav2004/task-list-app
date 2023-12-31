# Generated by Django 5.0.1 on 2023-12-31 08:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]