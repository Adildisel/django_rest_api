# Generated by Django 2.2.6 on 2019-10-24 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20191024_0647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parsercomments',
            name='video',
        ),
        migrations.DeleteModel(
            name='ParserVideoId',
        ),
    ]