# Generated by Django 2.0.2 on 2018-02-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packaging', '0002_auto_20180219_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='format_qty',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Total packaged quantity for this format in cases/units (NOT BBL).', max_digits=10, null=True, verbose_name='Packaged Units'),
        ),
    ]
