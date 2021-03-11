# Generated by Django 3.1 on 2021-03-11 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0022_season_max_team_members'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='round',
            options={'ordering': ['round_number', '-name']},
        ),
        migrations.RemoveField(
            model_name='round',
            name='bracket',
        ),
        migrations.DeleteModel(
            name='Bracket',
        ),
    ]
