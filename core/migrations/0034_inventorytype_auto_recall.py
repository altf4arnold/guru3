# Generated by Django 2.1.11 on 2019-08-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20190819_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorytype',
            name='auto_recall',
            field=models.BooleanField(default=False, verbose_name='Automatically recall rental devices of this type if they are assigned to an extension'),
        ),
    ]
