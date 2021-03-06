# Generated by Django 2.0.2 on 2018-03-07 18:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brewing', '0020_auto_20180302_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='plato_1_val',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='plato_1_vol',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='plato_2_val',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='plato_2_vol',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='plato_3_val',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='plato_3_vol',
        ),
        migrations.AddField(
            model_name='batch',
            name='d_rest',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='first_dry_hop',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='gravity_1',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Enter a gravity (plato).', max_digits=5, null=True, verbose_name='Gravity Log'),
        ),
        migrations.AddField(
            model_name='batch',
            name='gravity_1_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='batch',
            name='gravity_2',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Enter a gravity (plato).', max_digits=5, null=True, verbose_name='Gravity Log'),
        ),
        migrations.AddField(
            model_name='batch',
            name='gravity_2_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='batch',
            name='gravity_3',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Enter a gravity (plato).', max_digits=5, null=True, verbose_name='Gravity Log'),
        ),
        migrations.AddField(
            model_name='batch',
            name='gravity_3_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='batch',
            name='mash_temperature',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Mash Temperature', max_digits=5, null=True, verbose_name='Mash Temperature'),
        ),
        migrations.AddField(
            model_name='batch',
            name='postboil_gravity',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Post Boil Gravity', max_digits=5, null=True, verbose_name='Post Boil Gravity'),
        ),
        migrations.AddField(
            model_name='batch',
            name='postboil_volume',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Post Boil Volume', max_digits=5, null=True, verbose_name='Post Boil Volume'),
        ),
        migrations.AddField(
            model_name='batch',
            name='preboil_gravity',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Pre Boil Gravity', max_digits=5, null=True, verbose_name='Pre Boil Gravity'),
        ),
        migrations.AddField(
            model_name='batch',
            name='preboil_volume',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Pre Boil Volume', max_digits=5, null=True, verbose_name='Pre Boil Volume'),
        ),
        migrations.AddField(
            model_name='batch',
            name='second_dry_hop',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
