# Generated by Django 3.2.5 on 2021-08-26 18:29

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userposts', '0019_alter_userposts_postcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userposts',
            name='postContent',
            field=django_quill.fields.QuillField(null=True, verbose_name='Content'),
        ),
    ]