# Generated by Django 5.0.1 on 2023-12-31 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_task_completed_task_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date_time',
            new_name='last_reset',
        ),
    ]
