# Generated by Django 2.0.1 on 2018-03-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180225_2050_squashed_0005_auto_20180225_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='type',
            field=models.CharField(choices=[('SIP', 'SIP telephone'), ('DECT', 'DECT handset'), ('GSM', 'GSM handset'), ('GROUP', 'Callgroup'), ('SPECIAL', 'Special number (blocker)')], max_length=16, verbose_name='Type'),
        ),
    ]