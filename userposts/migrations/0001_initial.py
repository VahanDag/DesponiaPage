# Generated by Django 3.2.5 on 2021-10-18 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postTitle', models.CharField(max_length=100, verbose_name='Title')),
                ('postContent', tinymce.models.HTMLField(null=True, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of upload')),
                ('last_message', models.DateTimeField(blank=True, null=True)),
                ('answer_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='Answer Count')),
                ('post_views', models.IntegerField(default=0, null=True, verbose_name='post_views')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.category', verbose_name='Category')),
                ('last_message_username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_message_username', to=settings.AUTH_USER_MODEL, verbose_name='Last Message Username')),
                ('like_post', models.ManyToManyField(blank=True, related_name='like_post', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
        ),
        migrations.CreateModel(
            name='UserMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postMessages', tinymce.models.HTMLField(null=True, verbose_name='Messages')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of upload')),
                ('total_like', models.IntegerField(blank=True, default=0, null=True, verbose_name='Total Like')),
                ('like_message', models.ManyToManyField(blank=True, related_name='like_message', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userposts.userposts', verbose_name='Linked Post')),
                ('replies', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userposts.usermessages')),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
        ),
    ]
