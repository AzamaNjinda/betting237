# Generated by Django 4.2.7 on 2024-09-13 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0026_betfixture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betslip',
            name='bet_histories',
            field=models.ManyToManyField(blank=True, null=True, related_name='bet_slips', to='server.bethistory'),
        ),
    ]
