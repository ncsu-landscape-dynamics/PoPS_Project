# Generated by Django 3.1.1 on 2020-09-03 13:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pops', '0022_auto_20200318_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='pestinformation',
            name='arrival_location',
            field=models.CharField(blank=True, default=None, max_length=150, null=True, verbose_name='first location found in US (State)'),
        ),
        migrations.AddField(
            model_name='pestinformation',
            name='arrival_year',
            field=models.PositiveSmallIntegerField(blank=True, default=None, help_text='The first year that it was identified in the US.', null=True, validators=[django.core.validators.MinValueValidator(1700), django.core.validators.MaxValueValidator(2025)], verbose_name='first year found in US'),
        ),
        migrations.AddField(
            model_name='pestinformation',
            name='host_type',
            field=models.CharField(choices=[('ANIMAL', 'The pest or pathogen infects animals'), ('PLANT', 'The pest or pathogen infects plants')], default='PLANT', help_text='Choose what system type this pest/pathogen infects', max_length=30, verbose_name='host type'),
        ),
        migrations.AddField(
            model_name='pestinformation',
            name='invasive',
            field=models.BooleanField(default=True, help_text='Is the organism invasive in the US?', verbose_name='invasive'),
        ),
        migrations.AddField(
            model_name='pestinformation',
            name='organism_type',
            field=models.CharField(choices=[('PEST', 'The organism is a pest (e.g. insect)'), ('PATHOGEN', 'The organism is a pathogen (e.g. disease)')], default='PEST', help_text='Choose whether this is a pest or pathogen', max_length=30, verbose_name='organism type'),
        ),
    ]
