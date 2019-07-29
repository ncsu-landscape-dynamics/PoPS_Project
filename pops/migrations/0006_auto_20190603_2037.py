# Generated by Django 2.1.5 on 2019-06-04 00:37

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pops', '0005_auto_20190527_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='description',
            field=models.TextField(blank=True, default='Give your run a description.', help_text='Give your run a description.', max_length=300, null=True, verbose_name='run description'),
        ),
        migrations.AlterField(
            model_name='run',
            name='management_polygons',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='run',
            name='name',
            field=models.CharField(max_length=45, verbose_name='run name'),
        ),
        migrations.AlterField(
            model_name='run',
            name='random_seed',
            field=models.PositiveIntegerField(default=33, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='random seed'),
        ),
        migrations.AlterField(
            model_name='session',
            name='case_study',
            field=models.ForeignKey(help_text='Select a case study for this session.', on_delete=django.db.models.deletion.CASCADE, to='pops.CaseStudy', verbose_name='case study'),
        ),
        migrations.AlterField(
            model_name='session',
            name='name',
            field=models.CharField(help_text='Give your session a descriptive name.', max_length=150, verbose_name='session name'),
        ),
    ]
