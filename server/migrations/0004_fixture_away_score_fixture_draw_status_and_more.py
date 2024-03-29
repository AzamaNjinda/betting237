# Generated by Django 4.2.7 on 2023-12-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_fixture_date_fixture_league_fixture_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='away_score',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fixture',
            name='draw_status',
            field=models.CharField(blank=True, choices=[('up', 'up'), ('down', 'down')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='fixture',
            name='home_score',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fixture',
            name='home_win_status',
            field=models.CharField(blank=True, choices=[('up', 'up'), ('down', 'down')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='fixture',
            name='in_play',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='away_win',
            field=models.CharField(blank=True, choices=[('up', 'up'), ('down', 'down')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='fixture',
            name='league',
            field=models.CharField(blank=True, choices=[('PL', 'Premier League'), ('LL', 'La Liga'), ('BL', 'BundesLiga'), ('SA', 'Serie A'), ('L1', 'Legue 1'), ('UCL', 'UEFA Champions League'), ('UEL', 'UEFA Europa League')], max_length=3, null=True),
        ),
    ]
