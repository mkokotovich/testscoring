# Generated by Django 4.1.2 on 2022-10-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluators', '0002_rename_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
