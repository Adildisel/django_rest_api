# Generated by Django 2.2.6 on 2019-10-24 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_parsercomments_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='parsercomments',
            name='video',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.ParserVideoId', verbose_name='Данные видео'),
        ),
    ]