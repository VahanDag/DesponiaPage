# Generated by Django 3.2.5 on 2021-09-08 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_notifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='date',
        ),
    ]
