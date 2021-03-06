# Generated by Django 2.0.2 on 2018-02-22 21:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('brewing', '0009_auto_20180222_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='brix_2_vol',
            new_name='plato_2_vol',
        ),
        migrations.RenameField(
            model_name='batch',
            old_name='brix_3_vol',
            new_name='plato_3_vol',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='brite_tank',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='brix_1_val',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='brix_1_vol',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='brix_2_val',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='brix_3_val',
        ),
        migrations.AddField(
            model_name='batch',
            name='plato_1_val',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Initial Plato Reading.', max_digits=5, null=True, verbose_name='Initial Plato Reading'),
        ),
        migrations.AddField(
            model_name='batch',
            name='plato_1_vol',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Initial Plato Volume.', max_digits=5, null=True, verbose_name='Initial Plato Volume'),
        ),
        migrations.AddField(
            model_name='batch',
            name='plato_2_val',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Second Plato Reading.', max_digits=5, null=True, verbose_name='Second Plato Reading'),
        ),
        migrations.AddField(
            model_name='batch',
            name='plato_3_val',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Final Plato Reading.', max_digits=5, null=True, verbose_name='Final Plato Reading'),
        ),
        migrations.AddField(
            model_name='batch',
            name='transfer_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='batch',
            name='transfer_tank',
            field=models.ForeignKey(blank=True, default='', limit_choices_to={'container_type': 'A'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='brewing.Container', verbose_name='Brite Tank'),
        ),
    ]
