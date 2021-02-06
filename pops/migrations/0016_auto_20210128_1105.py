# Generated by Django 3.1.4 on 2021-01-28 16:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pops', '0015_auto_20210128_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='max_value',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='Maximum number of infected in a cell for final year', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)], verbose_name='maximum value within a cell in default run'),
        ),
    ]