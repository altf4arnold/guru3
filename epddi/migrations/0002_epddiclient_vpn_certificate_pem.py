# Generated by Django 3.0.5 on 2020-12-17 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epddi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='epddiclient',
            name='vpn_certificate_pem',
            field=models.TextField(blank=True, verbose_name='VPN Certificate'),
        ),
    ]
