# Generated by Django 3.1 on 2020-12-13 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='matches_csv_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='season',
            name='team_csv_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='circuit',
            name='tier',
            field=models.CharField(choices=[('1', 'Tier 1'), ('2', 'Tier 2'), ('3', 'Tier 3'), ('4', 'Tier 4'), ('0', 'No Tier')], max_length=1),
        ),
    ]
