# Generated by Django 2.0.2 on 2018-02-19 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewing', '0002_auto_20180219_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='abv',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Target ABV (%)', max_digits=4, null=True, verbose_name='ABV'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ibu',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Target IBU', max_digits=4, null=True, verbose_name='IBU'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='srm',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Target SRM', max_digits=4, null=True, verbose_name='SRM'),
        ),
    ]