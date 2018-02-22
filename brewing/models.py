from django.db import models
from django.utils import timezone

# For post-batch save signalling
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver



class MetaBase(models.Model):
    """
    Base recipe model which all other models inherit
    from. This model has fields and methods which
    are common for all models
    """
    name = models.CharField("name", max_length=100)
    cdt = models.DateTimeField("created", editable=False, auto_now_add=True)
    mdt = models.DateTimeField("modified", editable=False, auto_now=True)
    

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        app_label = "brewing"



class Container(MetaBase):
    '''
    Tank base class
    '''
    
    CONTAINER_TYPES = (
        ("F", "Fermentation"),
        ("B", "Brite"),
        ("A", "Aging")
    )

    capacity = models.DecimalField("Equipment Capactiy", max_digits=5, 
        decimal_places=2, help_text="""Maximum capacity of this container (in bbl).""")
    container_type = models.CharField("Container Type", max_length=100, choices=CONTAINER_TYPES, default="F")
    notes = models.TextField("notes", blank=True, null=True)




class Barrel(Container):
    '''
    Barrel class
    '''

    SPIRITS = (
        ("B", "Bourbon"),
        ("B/M", "Bourbon/Maple"),
        ("G", "Gin"), 
        ("R", "Rum"),
        ("T", "Tequila"),
        ("W", "Whiskey"),
        ("SMW", "Single Malt Whiskey")
    )

    MANUFACTURERS = (
        ("KC", "Kelvin Cooperage"),
        ("BS", "Black Swan"),
        ("U", "Unknown"),
        ("O", "Other")
    )

    DISTILLERS = (
        ("WR", "Woodfords Reserve"),
        ("RD", "River Driver"),
        ("MCD", "Maine Craft Distillery")
    )

    spirit_profile = models.CharField("Spirit profile", max_length=100, choices=SPIRITS, default="B/M")
    manufacturer = models.CharField("Manufacturer", max_length=100, choices=MANUFACTURERS, blank=True, null=True)
    distiller = models.CharField("Distiller", max_length=100, choices=DISTILLERS, blank=True, null=True)



class Entry(models.Model):
    '''
    Defines the entry class
    '''
    TYPE = (
        ("B", "Brix"),
        ("G", "Gravity"),
        ("T", "Transfer")
    )

    date = models.DateField(default=timezone.now, blank=True, null=True)


    def __str__(self):
        return str(self.date)



class Brix(Entry):
    '''
    Defines a brix reading:
    value (degrees brix) @ volume
    '''
    value = models.DecimalField("Degrees Brix", max_digits=14, decimal_places=2, help_text="Sugar content of an aqueous solution.")
    volume = models.DecimalField("Batch Volume (Hl)", max_digits=14, decimal_places=2, help_text="Batch volume at the time of this reading.")


    def __str__(self):
        return str(self.value) + " @ " + str(self.volume) + "(Hl)"



class Gravity(Entry):
    '''
    Defines a gravity reading:
    date, gravity
    '''
    value = models.DecimalField("Specific Gravity", max_digits=14, decimal_places=2, help_text="Specific Gravity/Relative Density.")


    def __str__(self):
        return str(self.value) + " | " + str(self.date)



class Transfer(Entry):
    '''
    Defines a transfer entry
    '''
    container = models.ForeignKey(Container, related_name='transfer_tank', on_delete=models.CASCADE, default='')
    cip = models.BooleanField('CIP?', default=False, help_text="Tick this box if the container was cleaned prior to transfer.")
    volume = models.DecimalField("Batch Volume (Hl)", max_digits=14, decimal_places=2, blank=True, null=True, help_text="Batch volume at the time of transfer.")


    def __str__(self):
        return str(self.date) + ", " + str(self.container) + ", CIP: " + str(self.cip)



class Batch(models.Model):
    '''
    Batches are comprised of the following attributes:
    brewer = models.CharField(choices)
    gyle = models.IntegerField(should be a number, and should be sequential )
    recipe = models.ForeignKey('Recipe')
    double_batch (boolean. Ticking this box creates a copy of the batch with the next sequential gyle)
    '''

    NAME = (
        ("sean", "Sean"),
        ("shea", "Shea"),
        ("ian", "Ian"),
        ("ron", "Ron"),
        ("brandon", "Brandon")
    )

    YEAST_TYPES = (
        ("001", "001"),
        ("3470", "3470"),
        ("other", "Other")
    )

    brew_date = models.DateField(default=timezone.now, blank=True, null=True)
    brewer = models.CharField("Brewer", max_length=100, choices=NAME, default="sean")
    asst_brewer = models.CharField("Assistant Brewer", max_length=100, blank=True, null=True)
    gyle = models.PositiveSmallIntegerField('Gyle #', primary_key=True)
    double_batch = models.BooleanField('Double-batch?', default=False, help_text="Tick this box to create a second batch on save.")
    current_tank = models.ForeignKey(Container, related_name='current_batch_tank', default='', verbose_name="Ferm. Tank", on_delete=models.CASCADE, blank=True, null=True)
    recipe = models.ForeignKey('Recipe', default='', on_delete=models.CASCADE, blank=True, null=True)
    brix_log = models.ManyToManyField(Brix, blank=True, null=True, help_text="Zero or more brix entries")
    gravity_log = models.ManyToManyField(Gravity, blank=True, null=True, help_text="Zero or more gravity entries")
    transfer_log = models.ManyToManyField(Transfer, blank=True, null=True, help_text="Zero or more transfer entries")
    cellaring_log = models.TextField("Cellaring Log", blank=True, null=True, help_text="Enter any cellaring notes here.")
    notes = models.TextField("Batch Notes", blank=True, null=True, help_text="Enter batch notes here.")
    yeast_type = models.CharField("Yeast Type", max_length=100, choices=YEAST_TYPES, default="001")
    yeast_gen = models.CharField("Yeast Generation", max_length=100, blank=True, null=True)
    yeast_origin_gyle = models.CharField("Yeast Origin Gyle", max_length=100, blank=True, null=True)
    yeast_log = models.TextField("Yeast Log", blank=True, null=True, help_text="Enter yeast notes here.")
    cdt = models.DateTimeField("created", editable=False, auto_now_add=True)
    mdt = models.DateTimeField("modified", editable=False, auto_now=True)


    def get_recipe(self):
        return str(self.recipe)


    def save(self, *args, **kwargs):
        if self.cdt == self.mdt:
            super().save(*args, **kwargs)  # Call the "real" save() method.
            if self.double_batch == True: # creates a duplicate record with the next sequential gyle #
                og_gyle = self.gyle
                self.pk = None
                self.gyle = og_gyle + 1
                super().save(*args, **kwargs)  # Call the "real" save() method.
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method. 


    def __str__(self):
        return str(self.gyle) + ": " + str(self.recipe)
        #return str(self.gyle)


    class Meta:
        verbose_name_plural = 'Batches'



class Fermentable(MetaBase):
    """
    The term "fermentable" encompasses all fermentable items that contribute 
    substantially to the beer including extracts, grains, sugars, honey, fruits.
    """
    
    TYPE = (
        ("grain", "Grain"),
        ("sugar", "Sugar"),
        ("extract", "Extract"),
        ("dry extract", "Dry extract"),
        ("adjunct", "Adjunct")
    )
    
    # NOTE: type is a reserved python word.
    ferm_type = models.CharField("fermentable type", max_length=12, choices=TYPE)
    amount = models.DecimalField("amount", max_digits=14, decimal_places=2, help_text="Weight of the fermentable, extract or sugar in pounds.")
    # NOTE: yield is a reserved python word.
    ferm_yield = models.DecimalField("yield percentage", max_digits=14, 
            decimal_places=9, blank=True, null=True, help_text="""Percent dry yield (fine grain) 
            for the grain, or the raw yield by weight if this is an 
            extract adjunct or sugar.""")
    color = models.DecimalField("color", max_digits=14, decimal_places=9,
            blank=True, null=True, help_text="""The color of the item in Lovibond Units 
            (SRM for liquid extracts).""")
    origin = models.CharField("origin country", max_length=100, blank=True, null=True)
    supplier = models.TextField("supplier", blank=True, null=True)
    notes = models.TextField("notes", blank=True, null=True)
    coarse_fine_diff = models.DecimalField("coarse/fine percentage", max_digits=14, 
            decimal_places=9, blank=True, null=True, help_text="""Percent difference 
            between the coarse grain yield and fine grain yield.  Only appropriate for 
            a "Grain" or "Adjunct" type, otherwise this value is ignored.""")
    moisture = models.DecimalField("moisture percentage", max_digits=14, 
            decimal_places=9, blank=True, null=True, help_text="""Percent 
            moisture in the grain. Only appropriate for a "Grain" or "Adjunct" type, 
            otherwise this value is ignored.""")
    diastatic_power = models.DecimalField("diastatic power", max_digits=14, 
            decimal_places=9, blank=True, null=True, help_text="""The diastatic power 
            of the grain as measured in "Lintner" units. Only appropriate for a 
            "Grain" or "Adjunct" type, otherwise this value is ignored.""")
    protein = models.DecimalField("protein percentage", max_digits=14, 
            decimal_places=9, blank=True, null=True, help_text="""The percent 
            protein in the grain. Only appropriate for a "Grain" or "Adjunct" type, 
            otherwise this value is ignored.""")
    max_in_batch = models.DecimalField("max percentage per batch", max_digits=14, 
            decimal_places=9, blank=True, null=True, help_text="""The recommended 
            maximum percentage (by weight) this ingredient should represent in a 
            batch of beer.""")
    recommend_mash = models.NullBooleanField("recommended mash", default=False, 
            blank=True, null=True, help_text="""True if it is recommended the grain 
            be mashed, False if it can be steeped. A value of True is only appropriate 
            for a "Grain" or "Adjunct" types. The default value is False. Note that 
            this does NOT indicate whether the grain is mashed or not – it is only 
            a recommendation used in recipe formulation.""")
    ibu_gal_per_lb = models.DecimalField("bitterness (IBU*gal/lb)", max_digits=14, 
            decimal_places=9, blank=True, null=True, help_text="""For hopped extracts 
            only - an estimate of the number of IBUs per pound of extract in a gallon 
            of water. To convert to IBUs we multiply this number by the "Amount" 
            field (in pounds) and divide by the number of gallons in the batch. 
            Based on a sixty minute boil. Only suitable for use with an "Extract" type, 
            otherwise this value is ignored.""")


    def __str__(self):
        return str(self.amount) + "# " + self.name
    

    
class Hop(MetaBase):
    """
    The “Hop” identifier is used to define all varieties of hops.
    """
    USE = (
        ("@ 60 Minutes", "@ 60 Minutes"),
        ("@ 10 Minutes", "@ 10 Minutes"),
        ("@ 5 Minutes", "@ 5 Minutes"),
        ("@ Whirlpool", "@ Whirlpool"),
        ("@ First Dry-Hop", "@ First Dry-Hop"),
        ("@ Second Dry-Hop", "@ Second Dry-Hop")
    )

    amount = models.DecimalField("amount", max_digits=14, decimal_places=2,
            help_text="Weight in pounds of the hops used in the recipe.")
    use = models.CharField("usage", max_length=50, choices=USE,
            help_text="""The phase at which this hop is added.""")
    notes = models.TextField("notes", blank=True, null=True)


    def __str__(self):
        return str(self.amount) + "# " + self.name + self.use




class Salt(MetaBase):
    """
    The “Salt” identifier is used to define all varieties of salts.
    """

    amount = models.DecimalField("amount", max_digits=14, decimal_places=2,
            help_text="Weight in ounces of the salt used in the recipe.")
    notes = models.TextField("notes", blank=True, null=True)

    def __str__(self):
        return str(self.amount) + "# " + self.name



class Misc(MetaBase):
    """
    Database model for various items
    """
    
    TYPE = (
        ("spice", "Spice"),
        ("fining", "Fining"),
        ("water agent", "Water agent"),
        ("herb", "Herb"),
        ("flavor", "Flavor"),
        ("other", "Other")
    )
    
    USE = (
       ("boil", "Boil"),
       ("mash", "Mash"),
       ("primary", "Primary"),
       ("secondary", "Secondary"),
       ("bottling", "Bottling")
    )
    
    # NOTE: type is a reserved python word.
    misc_type = models.CharField("hop type", max_length=12, choices=TYPE, default=4)
    use = models.CharField("hop use", max_length=12, choices=USE, default=2)
    time = models.DecimalField("time", max_digits=14, decimal_places=9,
            help_text="Amount of time the misc was boiled, steeped, mashed, etc in minutes.")
    amount = models.DecimalField("yield percentage", max_digits=14, decimal_places=2,
            help_text="""Amount of item used. The default measurements are by weight, 
            but this may be the measurement in volume units if AMOUNT_IS_WEIGHT is set 
            to TRUE for this record. For liquid items this is liters, for solid the  
            weight is measured in kilograms.""")
    amount_is_weight = models.BooleanField("amount is weight", default=False,
            help_text="""TRUE if the amount measurement is a weight measurement and FALSE if 
            the amount is a volume measurement.""")
    use_for = models.TextField("use for", blank=True, null=True,
            help_text="Short description of what the ingredient is used for in text")
    notes = models.TextField("notes", blank=True, null=True,
            help_text="Detailed notes on the item including usage.")


    def __str__(self):
        return str(self.amount) + "# " + self.name

    
    
class Yeast(MetaBase):
    """
    Database model for yeast
    """
    
    TYPE = (
        ("ale", "Ale"),
        ("lager", "Lager"),
        ("wheat", "Wheat"),
        ("wine", "Wine"),
        ("champagne", "Champagne")
    )
    
    FORM = (
        ("liquid", "Liquid"),
        ("dry", "Dry"),
        ("slant", "Slant"),
        ("culture", "Culture")
    )
    
    FLOCCULATION = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("very high", "Very high")
    )
    
    # NOTE: type is a reserved python word.
    yeast_type = models.CharField("yeast type", max_length=12, choices=TYPE, default=1)
    form = models.CharField("yeast form", max_length=12, choices=FORM, default=1)
    amount = models.DecimalField("amount", max_digits=14, decimal_places=2,
            help_text="""The amount of yeast, measured in liters. For a starter this is the 
            size of the starter. If the flag AMOUNT_IS_WEIGHT is set to TRUE then this 
            measurement is in kilograms and not liters.""")
    amount_is_weight = models.BooleanField("amount is weight or litres", default=False,
            help_text="""TRUE if the amount measurement is a weight measurement and FALSE 
            if the amount is a volume measurement.  Default value (if not present) is 
            assumed to be FALSE – therefore the yeast measurement is a liquid amount 
            by default.""")
    laboratory = models.CharField("laboratory name", max_length=100, blank=True, null=True)
    product_id = models.CharField("product id", max_length=100, blank=True, null=True,
            help_text="""The manufacturer’s product ID label or number that identifies this 
            particular strain of yeast.""")
    min_temperature = models.DecimalField("min temperature", max_digits=14, 
            decimal_places=9, blank=True, null=True, help_text="""The minimum 
            recommended temperature for fermenting this yeast strain in degrees 
            Celsius.""")
    max_temperature = models.DecimalField("max temperature", max_digits=14, 
            decimal_places=9, blank=True, null=True, help_text="""The maximum 
            recommended temperature for fermenting this yeast strain in Celsius.""")
    flocculation = models.CharField("yeast form", max_length=12, choices=FLOCCULATION, 
                                    default=1, blank=True, null=True)
    attenuation = models.DecimalField("attenuation percentage", max_digits=14, 
            decimal_places=9, blank=True, null=True, help_text="""Average 
            attenuation for this yeast strain.""")
    notes = models.TextField("notes", blank=True, null=True)
    best_for = models.TextField("best for", blank=True, null=True,
            help_text="Styles or types of beer this yeast strain is best suited for.")
    times_cultured = models.PositiveSmallIntegerField("times recultured", 
            blank=True, null=True, help_text="""Number of times this yeast has 
            been reused as a harvested culture. This number should be zero if this 
            is a product directly from the manufacturer.""")
    max_reuse = models.PositiveSmallIntegerField("max recultures", blank=True, 
            null=True, help_text="""Recommended of times this yeast can be reused 
            (recultured from a previous batch)""")
    add_to_secondary = models.BooleanField("amount is weight", default=False,
            help_text="""Flag denoting that this yeast was added for a secondary (or later) 
            fermentation as opposed to the primary fermentation. Useful if one uses two              
            or more yeast strains for a single brew (eg: Lambic). Default value is FALSE.""")


    def __str__(self):
        return str(self.amount) + "# " + self.name


class Recipe(MetaBase):
    """
    Database model for reciepes
    """
    pre_boil_batch_size = models.DecimalField("pre boil batch size", max_digits=14, decimal_places=9, help_text="Target pre boil batch size in hectoliters.")
    pre_boil_gravity = models.DecimalField("pre boil gravity", max_digits=14, decimal_places=9, help_text="Target pre boil gravity(Brix).")
    fermentation_temp = models.DecimalField("fermentation temperature", max_digits=5, decimal_places=2, help_text="Target fermentation temperature (F)")
    mash_temp = models.DecimalField("mash temperature", max_digits=5, decimal_places=2, help_text="Target mash temperature (F)")
    strike_temperature = models.DecimalField("strike temperature", max_digits=5, decimal_places=2, help_text="Target strike temperature (F)")
    strike = models.DecimalField("strike", max_digits=5, decimal_places=2, help_text="Target strike value (Gal)")
    sparge = models.DecimalField("sparge", max_digits=5, decimal_places=2, help_text="Target sparge (Gal)")
    ibu = models.DecimalField("IBU", blank=True, null=True, max_digits=4, decimal_places=2, help_text="Target IBU")
    abv = models.DecimalField("ABV", blank=True, null=True, max_digits=4, decimal_places=2, help_text="Target ABV (%)")
    srm = models.DecimalField("SRM", blank=True, null=True, max_digits=4, decimal_places=2, help_text="Target SRM")
    hops = models.ManyToManyField(Hop, blank=True, null=True, help_text="Zero or more hops")
    fermentables = models.ManyToManyField(Fermentable, blank=True, null=True, help_text="Zero or more fermentable ingredients")
    salts = models.ManyToManyField(Salt, blank=True, null=True, help_text="Zero or more salts")
    miscs = models.ManyToManyField(Misc, blank=True, null=True, help_text="Zero or more misc records")
    yeasts = models.ManyToManyField(Yeast, blank=True, null=True, help_text="Zero or more yeast records")
    notes = models.TextField("notes", blank=True, null=True)
