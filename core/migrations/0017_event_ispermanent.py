# Generated by Django 2.0.9 on 2018-11-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20181014_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='isPermanent',
            field=models.BooleanField(default=False, verbose_name='This event is a permanent event'),
            preserve_default=False,
        ),
    ]
