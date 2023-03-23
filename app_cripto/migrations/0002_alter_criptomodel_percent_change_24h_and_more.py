# Generated by Django 4.1.5 on 2023-03-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cripto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criptomodel',
            name='percent_change_24h',
            field=models.CharField(max_length=20, verbose_name='Price change for 24 hours'),
        ),
        migrations.AlterField(
            model_name='criptomodel',
            name='price',
            field=models.CharField(max_length=20, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='criptomodel',
            name='volume_24h',
            field=models.CharField(max_length=20, verbose_name='Selling volume for 24 hours'),
        ),
        migrations.AlterField(
            model_name='criptomodel',
            name='volume_change_24h',
            field=models.CharField(max_length=20, verbose_name='Selling volume change for 24 hours'),
        ),
    ]
