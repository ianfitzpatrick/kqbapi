# Generated by Django 3.1 on 2020-12-14 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_auto_20201214_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='number',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='set',
            name='number',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
