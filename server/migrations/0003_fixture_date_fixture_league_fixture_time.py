# Generated by Django 4.2.7 on 2023-12-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_fixture'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fixture',
            name='league',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fixture',
            name='time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
