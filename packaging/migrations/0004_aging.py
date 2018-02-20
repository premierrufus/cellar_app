# Generated by Django 2.0.2 on 2018-02-20 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brewing', '0007_barrel'),
        ('packaging', '0003_auto_20180220_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packager', models.CharField(blank=True, choices=[('tyler', 'Tyler'), ('ron', 'Ron'), ('chris', 'Chris'), ('shea', 'Shea'), ('ian', 'Ian'), ('brandon', 'Brandon')], max_length=100, null=True, verbose_name='packager')),
                ('barrel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brewing.Barrel')),
                ('batches', models.ManyToManyField(blank=True, help_text='Batches sourced.', null=True, to='brewing.Batch', verbose_name='Source Batches')),
            ],
        ),
    ]
