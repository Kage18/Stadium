# Generated by Django 2.1.4 on 2019-12-10 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvatarImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='customerprofile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='avatar',
            field=models.ManyToManyField(to='users.AvatarImage'),
        ),
    ]
