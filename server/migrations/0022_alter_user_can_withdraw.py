# Generated by Django 4.2.7 on 2024-03-25 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0021_withdrawal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='can_withdraw',
            field=models.BooleanField(default=True),
        ),
    ]