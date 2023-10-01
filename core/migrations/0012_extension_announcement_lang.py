# Generated by Django 2.0.3 on 2018-06-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_event_announcement_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='extension',
            name='announcement_lang',
            field=models.CharField(choices=[('DE-DE', 'Deutsch (Deutschland)'), ('EN-GB', 'English (GB)'), ('EN-US', 'English (US)')], default='DE-DE', max_length=5, verbose_name='Announcement Language'),
        ),
    ]