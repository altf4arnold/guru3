# Generated by Django 2.1.5 on 2019-07-23 17:57

import core
from django.db import migrations


def reinit_event_orga_keys(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Event = apps.get_model("core", "Event")
    db_alias = schema_editor.connection.alias
    events = Event.objects.using(db_alias).all()
    for event in events:
        event.orgaKey = core.models._generate_orgakey()
        event.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20190723_1757'),
    ]

    operations = [
        migrations.RunPython(reinit_event_orga_keys),
    ]
