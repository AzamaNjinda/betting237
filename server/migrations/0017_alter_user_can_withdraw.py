# Generated by Django 4.2.7 on 2024-02-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0016_betslip_is_combo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='can_withdraw',
            field=models.BooleanField(default=False),
        ),
    ]