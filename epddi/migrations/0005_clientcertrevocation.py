# Generated by Django 3.0.5 on 2020-12-18 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epddi', '0004_auto_20201218_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCertRevocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_serial_hex', models.CharField(max_length=64, verbose_name='Serial number of revoked cert in hex')),
                ('revocation_time', models.DateTimeField(auto_now_add=True, verbose_name='Revocation time')),
                ('revocation_reason', models.CharField(max_length=64, verbose_name='Reason for revocation')),
            ],
        ),
    ]