# Generated by Django 3.1.1 on 2020-10-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_emaillistentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='emaillistentry',
            name='email_confirmed',
            field=models.BooleanField(default=False, verbose_name='email confirmed'),
        ),
    ]