# Generated by Django 2.1.4 on 2019-11-11 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_auto_20191111_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('shown', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MerchImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('merch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merch.Merchandise')),
            ],
        ),
        migrations.CreateModel(
            name='MerchUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.IntegerField()),
                ('merch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merch.Merchandise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CustomerProfile')),
            ],
        ),
    ]