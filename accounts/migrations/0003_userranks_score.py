# Generated by Django 3.2.5 on 2021-09-01 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userranks'),
    ]

    operations = [
        migrations.AddField(
            model_name='userranks',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Score'),
        ),
    ]
