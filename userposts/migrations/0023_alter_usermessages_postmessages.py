# Generated by Django 3.2.5 on 2021-08-28 01:16

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userposts', '0022_alter_userposts_postcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessages',
            name='postMessages',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Message'),
        ),
    ]