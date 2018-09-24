# Generated by Django 2.0.2 on 2018-09-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewing', '0023_auto_20180917_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='mash_ph',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Enter mash ph.', max_digits=5, null=True, verbose_name='Mash ph'),
        ),
        migrations.AddField(
            model_name='batch',
            name='pre_boil_ph',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Enter pre boil ph.', max_digits=5, null=True, verbose_name='Pre Boil ph'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='brewer',
            field=models.CharField(choices=[('sean', 'Sean'), ('shea', 'Shea'), ('ian', 'Ian'), ('richard', 'Richard')], default='sean', max_length=100, verbose_name='Brewer'),
        ),
    ]
