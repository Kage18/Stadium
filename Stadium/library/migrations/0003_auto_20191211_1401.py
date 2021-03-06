# Generated by Django 2.1.4 on 2019-12-11 14:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20191116_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rom',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game_owned',
            name='hours_played',
            field=models.IntegerField(default=0),
        ),
    ]
