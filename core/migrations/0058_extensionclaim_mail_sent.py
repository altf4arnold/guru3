# Generated by Django 3.0.5 on 2020-05-02 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_old_ringback_are_converted__20200502_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='extensionclaim',
            name='mail_sent',
            field=models.BooleanField(default=False),
        ),
    ]
