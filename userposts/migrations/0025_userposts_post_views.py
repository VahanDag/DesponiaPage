# Generated by Django 3.2.5 on 2021-09-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userposts', '0024_auto_20210828_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='userposts',
            name='post_views',
            field=models.IntegerField(default=0, null=True, verbose_name='post_views'),
        ),
    ]
