# Generated by Django 2.2.4 on 2019-09-04 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pops', '0016_hostdata_host_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicdata',
            name='number_infected',
            field=models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='number_infected'),
        ),
    ]