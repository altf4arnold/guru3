# Generated by Django 2.0.1 on 2018-02-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='useEncryption',
            field=models.BooleanField(default=False, verbose_name='Use encryption'),
            preserve_default=False,
        ),
    ]
