# Generated by Django 3.1.4 on 2021-01-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pops', '0010_run_r_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pest',
            name='model_type',
            field=models.CharField(blank=True, choices=[('SI', 'Susceptible Infected'), ('SEI', 'Susceptible Exposed Infected'), ('SEID', 'Susceptible Exposed Infected Diseased')], default='SI', help_text='What type of model do you want to use?', max_length=20, verbose_name='model type'),
        ),
    ]