# Generated by Django 2.0.2 on 2018-02-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('double_batch', models.BooleanField(verbose_name='Double-batch?')),
                ('gyle', models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='Gyle #')),
            ],
            options={
                'verbose_name_plural': 'Batches',
            },
        ),
        migrations.CreateModel(
            name='Fermentable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('cdt', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('mdt', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('ferm_type', models.CharField(choices=[('grain', 'Grain'), ('sugar', 'Sugar'), ('extract', 'Extract'), ('dry extract', 'Dry extract'), ('adjunct', 'Adjunct')], max_length=12, verbose_name='fermentable type')),
                ('amount', models.DecimalField(decimal_places=9, help_text='Weight of the fermentable, extract or sugar in pounds.', max_digits=14, verbose_name='amount')),
                ('ferm_yield', models.DecimalField(blank=True, decimal_places=9, help_text='Percent dry yield (fine grain) \n            for the grain, or the raw yield by weight if this is an \n            extract adjunct or sugar.', max_digits=14, null=True, verbose_name='yield percentage')),
                ('color', models.DecimalField(blank=True, decimal_places=9, help_text='The color of the item in Lovibond Units \n            (SRM for liquid extracts).', max_digits=14, null=True, verbose_name='color')),
                ('origin', models.CharField(blank=True, max_length=100, null=True, verbose_name='origin country')),
                ('supplier', models.TextField(blank=True, null=True, verbose_name='supplier')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('coarse_fine_diff', models.DecimalField(blank=True, decimal_places=9, help_text='Percent difference \n            between the coarse grain yield and fine grain yield.  Only appropriate for \n            a "Grain" or "Adjunct" type, otherwise this value is ignored.', max_digits=14, null=True, verbose_name='coarse/fine percentage')),
                ('moisture', models.DecimalField(blank=True, decimal_places=9, help_text='Percent \n            moisture in the grain. Only appropriate for a "Grain" or "Adjunct" type, \n            otherwise this value is ignored.', max_digits=14, null=True, verbose_name='moisture percentage')),
                ('diastatic_power', models.DecimalField(blank=True, decimal_places=9, help_text='The diastatic power \n            of the grain as measured in "Lintner" units. Only appropriate for a \n            "Grain" or "Adjunct" type, otherwise this value is ignored.', max_digits=14, null=True, verbose_name='diastatic power')),
                ('protein', models.DecimalField(blank=True, decimal_places=9, help_text='The percent \n            protein in the grain. Only appropriate for a "Grain" or "Adjunct" type, \n            otherwise this value is ignored.', max_digits=14, null=True, verbose_name='protein percentage')),
                ('max_in_batch', models.DecimalField(blank=True, decimal_places=9, help_text='The recommended \n            maximum percentage (by weight) this ingredient should represent in a \n            batch of beer.', max_digits=14, null=True, verbose_name='max percentage per batch')),
                ('recommend_mash', models.NullBooleanField(default=False, help_text='True if it is recommended the grain \n            be mashed, False if it can be steeped. A value of True is only appropriate \n            for a "Grain" or "Adjunct" types. The default value is False. Note that \n            this does NOT indicate whether the grain is mashed or not – it is only \n            a recommendation used in recipe formulation.', verbose_name='recommended mash')),
                ('ibu_gal_per_lb', models.DecimalField(blank=True, decimal_places=9, help_text='For hopped extracts \n            only - an estimate of the number of IBUs per pound of extract in a gallon \n            of water. To convert to IBUs we multiply this number by the "Amount" \n            field (in pounds) and divide by the number of gallons in the batch. \n            Based on a sixty minute boil. Only suitable for use with an "Extract" type, \n            otherwise this value is ignored.', max_digits=14, null=True, verbose_name='bitterness (IBU*gal/lb)')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('cdt', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('mdt', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('amount', models.DecimalField(decimal_places=9, help_text='Weight in pounds of the hops used in the recipe.', max_digits=14, verbose_name='amount')),
                ('use', models.CharField(choices=[('@ 60 Minutes', '@ 60 Minutes'), ('@ 10 Minutes', '@ 10 Minutes'), ('@ 5 Minutes', '@ 5 Minutes'), ('@ Whirlpool', '@ Whirlpool'), ('@ First Dry-Hop', '@ First Dry-Hop'), ('@ Second Dry-Hop', '@ Second Dry-Hop')], help_text='The phase at which this hop is added.', max_length=50, verbose_name='usage')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('origin', models.CharField(blank=True, max_length=100, null=True, verbose_name='origin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Misc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('cdt', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('mdt', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('misc_type', models.CharField(choices=[('spice', 'Spice'), ('fining', 'Fining'), ('water agent', 'Water agent'), ('herb', 'Herb'), ('flavor', 'Flavor'), ('other', 'Other')], default=4, max_length=12, verbose_name='hop type')),
                ('use', models.CharField(choices=[('boil', 'Boil'), ('mash', 'Mash'), ('primary', 'Primary'), ('secondary', 'Secondary'), ('bottling', 'Bottling')], default=2, max_length=12, verbose_name='hop use')),
                ('time', models.DecimalField(decimal_places=9, help_text='Amount of time the misc was boiled, steeped, mashed, etc in minutes.', max_digits=14, verbose_name='time')),
                ('amount', models.DecimalField(decimal_places=9, help_text='Amount of item used. The default measurements are by weight, \n            but this may be the measurement in volume units if AMOUNT_IS_WEIGHT is set \n            to TRUE for this record. For liquid items this is liters, for solid the  \n            weight is measured in kilograms.', max_digits=14, verbose_name='yield percentage')),
                ('amount_is_weight', models.BooleanField(default=False, help_text='TRUE if the amount measurement is a weight measurement and FALSE if \n            the amount is a volume measurement.', verbose_name='amount is weight')),
                ('use_for', models.TextField(blank=True, help_text='Short description of what the ingredient is used for in text', null=True, verbose_name='use for')),
                ('notes', models.TextField(blank=True, help_text='Detailed notes on the item including usage.', null=True, verbose_name='notes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('cdt', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('mdt', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('pre_boil_batch_size', models.DecimalField(decimal_places=9, help_text='Target pre boil batch size in hectoliters.', max_digits=14, verbose_name='pre boil batch size')),
                ('pre_boil_gravity', models.DecimalField(decimal_places=9, help_text='Target pre boil gravity(Brix).', max_digits=14, verbose_name='pre boil gravity')),
                ('fermentation_temp', models.DecimalField(decimal_places=2, help_text='Target fermentation temperature (F)', max_digits=5, verbose_name='fermentation temperature')),
                ('mash_temp', models.DecimalField(decimal_places=2, help_text='Target mash temperature (F)', max_digits=5, verbose_name='mash temperature')),
                ('strike_temperature', models.DecimalField(decimal_places=2, help_text='Target strike temperature (F)', max_digits=5, verbose_name='strike temperature')),
                ('strike', models.DecimalField(decimal_places=2, help_text='Target strike value (Gal)', max_digits=5, verbose_name='strike')),
                ('sparge', models.DecimalField(decimal_places=2, help_text='Target sparge (Gal)', max_digits=5, verbose_name='sparge')),
                ('ibu', models.DecimalField(decimal_places=2, help_text='Target IBU', max_digits=4, verbose_name='IBU')),
                ('abv', models.DecimalField(decimal_places=2, help_text='Target ABV (%)', max_digits=4, verbose_name='ABV')),
                ('srm', models.DecimalField(decimal_places=2, help_text='Target SRM', max_digits=4, verbose_name='SRM')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('fermentables', models.ManyToManyField(blank=True, help_text='Zero or more fermentable ingredients', null=True, to='brewing.Fermentable')),
                ('hops', models.ManyToManyField(blank=True, help_text='Zero or more hops', null=True, to='brewing.Hop')),
                ('miscs', models.ManyToManyField(blank=True, help_text='Zero or more misc records', null=True, to='brewing.Misc')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Salt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('cdt', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('mdt', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('amount', models.DecimalField(decimal_places=9, help_text='Weight in ounces of the salt used in the recipe.', max_digits=14, verbose_name='amount')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Yeast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('cdt', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('mdt', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('yeast_type', models.CharField(choices=[('ale', 'Ale'), ('lager', 'Lager'), ('wheat', 'Wheat'), ('wine', 'Wine'), ('champagne', 'Champagne')], default=1, max_length=12, verbose_name='yeast type')),
                ('form', models.CharField(choices=[('liquid', 'Liquid'), ('dry', 'Dry'), ('slant', 'Slant'), ('culture', 'Culture')], default=1, max_length=12, verbose_name='yeast form')),
                ('amount', models.DecimalField(decimal_places=9, help_text='The amount of yeast, measured in liters. For a starter this is the \n            size of the starter. If the flag AMOUNT_IS_WEIGHT is set to TRUE then this \n            measurement is in kilograms and not liters.', max_digits=14, verbose_name='amount')),
                ('amount_is_weight', models.BooleanField(default=False, help_text='TRUE if the amount measurement is a weight measurement and FALSE \n            if the amount is a volume measurement.  Default value (if not present) is \n            assumed to be FALSE – therefore the yeast measurement is a liquid amount \n            by default.', verbose_name='amount is weight or litres')),
                ('laboratory', models.CharField(blank=True, max_length=100, null=True, verbose_name='laboratory name')),
                ('product_id', models.CharField(blank=True, help_text='The manufacturer’s product ID label or number that identifies this \n            particular strain of yeast.', max_length=100, null=True, verbose_name='product id')),
                ('min_temperature', models.DecimalField(blank=True, decimal_places=9, help_text='The minimum \n            recommended temperature for fermenting this yeast strain in degrees \n            Celsius.', max_digits=14, null=True, verbose_name='min temperature')),
                ('max_temperature', models.DecimalField(blank=True, decimal_places=9, help_text='The maximum \n            recommended temperature for fermenting this yeast strain in Celsius.', max_digits=14, null=True, verbose_name='max temperature')),
                ('flocculation', models.CharField(blank=True, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('very high', 'Very high')], default=1, max_length=12, null=True, verbose_name='yeast form')),
                ('attenuation', models.DecimalField(blank=True, decimal_places=9, help_text='Average \n            attenuation for this yeast strain.', max_digits=14, null=True, verbose_name='attenuation percentage')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('best_for', models.TextField(blank=True, help_text='Styles or types of beer this yeast strain is best suited for.', null=True, verbose_name='best for')),
                ('times_cultured', models.PositiveSmallIntegerField(blank=True, help_text='Number of times this yeast has \n            been reused as a harvested culture. This number should be zero if this \n            is a product directly from the manufacturer.', null=True, verbose_name='times recultured')),
                ('max_reuse', models.PositiveSmallIntegerField(blank=True, help_text='Recommended of times this yeast can be reused \n            (recultured from a previous batch)', null=True, verbose_name='max recultures')),
                ('add_to_secondary', models.BooleanField(default=False, help_text='Flag denoting that this yeast was added for a secondary (or later) \n            fermentation as opposed to the primary fermentation. Useful if one uses two              \n            or more yeast strains for a single brew (eg: Lambic). Default value is FALSE.', verbose_name='amount is weight')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='salts',
            field=models.ManyToManyField(blank=True, help_text='Zero or more salts', null=True, to='brewing.Salt'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='yeasts',
            field=models.ManyToManyField(blank=True, help_text='Zero or more yeast records', null=True, to='brewing.Yeast'),
        ),
    ]
