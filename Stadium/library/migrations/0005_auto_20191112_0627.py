# Generated by Django 2.1.4 on 2019-11-12 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191111_1716'),
        ('library', '0004_auto_20191112_0624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game_owned',
            name='customer',
        ),
        migrations.AddField(
            model_name='game_owned',
            name='customer',
            field=models.ManyToManyField(to='users.CustomerProfile'),
        ),
        migrations.RemoveField(
            model_name='game_owned',
            name='game',
        ),
        migrations.AddField(
            model_name='game_owned',
            name='game',
            field=models.ManyToManyField(to='library.game'),
        ),
    ]