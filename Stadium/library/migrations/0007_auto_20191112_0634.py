# Generated by Django 2.1.4 on 2019-11-12 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191111_1716'),
        ('library', '0006_auto_20191112_0631'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='game_owned',
            unique_together={('customer', 'game')},
        ),
    ]