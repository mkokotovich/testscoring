# Generated by Django 2.1 on 2018-08-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_auto_20180824_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_type',
            field=models.CharField(choices=[('cbcl_6_18', 'cbcl_6_18'), ('cbcl_1_5', 'cbcl_1_5')], max_length=16),
        ),
    ]