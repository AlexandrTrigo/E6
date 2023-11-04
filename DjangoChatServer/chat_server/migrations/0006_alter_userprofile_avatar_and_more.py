# Generated by Django 4.0.3 on 2022-04-08 19:53

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat_server', '0005_userprofile_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='djangochatserver/default.jpg', upload_to='djangochatserver'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_small',
            field=easy_thumbnails.fields.ThumbnailerImageField(default='djangochatserver/default_small.jpg', upload_to='djangochatserver'),
        ),
    ]
