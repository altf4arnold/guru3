# Generated by Django 3.0.5 on 2020-05-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_auto_20200426_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='processed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='audiofile',
            name='processing_error',
            field=models.BooleanField(default=False),
        ),
    ]