# Generated by Django 2.2.4 on 2019-08-26 20:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pops', '0013_auto_20190826_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='output',
            name='susceptible_map',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]