# Generated by Django 3.2.5 on 2021-10-15 23:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_profile_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='signature',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Signature'),
        ),
    ]