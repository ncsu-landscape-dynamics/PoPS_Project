# Generated by Django 2.2.4 on 2019-09-01 16:41

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pops', '0015_auto_20190830_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostdata',
            name='host_map',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
