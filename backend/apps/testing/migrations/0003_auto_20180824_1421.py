# Generated by Django 2.1 on 2018-08-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0002_auto_20180822_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='item',
            name='group',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]