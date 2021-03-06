# Generated by Django 2.0.2 on 2018-02-22 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brewing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='cip',
            field=models.BooleanField(default=False, help_text='Tick this box if the container was cleaned prior to transfer.', verbose_name='CIP?'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='container',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='transfer_tank', to='brewing.Container'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Batch volume at the time of transfer.', max_digits=14, null=True, verbose_name='Batch Volume (Hl)'),
        ),
        migrations.RemoveField(
            model_name='batch',
            name='brix_log',
        ),
        migrations.AddField(
            model_name='batch',
            name='brix_log',
            field=models.ManyToManyField(blank=True, help_text='Zero or more brix entries', null=True, to='brewing.Brix'),
        ),
        migrations.RemoveField(
            model_name='batch',
            name='gravity_log',
        ),
        migrations.AddField(
            model_name='batch',
            name='gravity_log',
            field=models.ManyToManyField(blank=True, help_text='Zero or more gravity entries', null=True, to='brewing.Gravity'),
        ),
        migrations.RemoveField(
            model_name='batch',
            name='transfer_log',
        ),
        migrations.AddField(
            model_name='batch',
            name='transfer_log',
            field=models.ManyToManyField(blank=True, help_text='Zero or more transfer entries', null=True, to='brewing.Transfer'),
        ),
    ]
