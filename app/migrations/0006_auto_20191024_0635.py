# Generated by Django 2.2.6 on 2019-10-24 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191024_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parsercomments',
            name='video',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='app.ParserVideoId', verbose_name='Данные видео'),
        ),
    ]
