# Generated by Django 3.2.5 on 2021-10-15 23:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('userposts', '0035_alter_usermessages_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userposts',
            name='postContent',
            field=tinymce.models.HTMLField(null=True, verbose_name='Content'),
        ),
    ]