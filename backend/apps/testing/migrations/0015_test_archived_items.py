# Generated by Django 2.2 on 2019-05-24 16:09

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0014_auto_20190425_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='archived_items',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=list),
        ),
    ]
