# Generated by Django 2.1.7 on 2019-03-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_sensor1client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor1client',
            name='time',
            field=models.CharField(max_length=35, verbose_name='time instant'),
        ),
    ]