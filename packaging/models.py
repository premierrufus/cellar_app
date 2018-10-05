from django.db import models
from django.utils import timezone
from decimal import *
from brewing.models import Barrel, Batch


# Global Model Variables

PACKAGER_NAME = (
    ("tyler", "Tyler"),
    ("ron", "Ron"),
    ("chris", "Chris"),
    ("shea", "Shea"),
    ("ian", "Ian"),
    ("brandon", "Brandon")
)


# Global Packaging Methods

def to_bbl(f, q):
        """
        Takes two arguments: format(f), quantity(q)
        Returns value(v) as a Decimal object, rounded to two places. 

        """
        BBL_CONVERSION_MAPPING = {
            '12oz/CS': 0.07258064516129033,
            '16oz/CS': 0.0967741935483871,
            '375ml/CS': 0.038387096774193545,
            '500ml/CS': 0.05112903225806451,
            '750ml/CS': 0.07677419354838709,
            '1/6bbl': 0.16666666666666666,
            '1/4bbl': 0.25,
            '1/2bbl': 0.5,
            '50l': 0.426,
            'Firkin (10.8g)': 0.34838709677419355,
            'Pin (5.4g)': 0.17419354838709677
        }

        if f in BBL_CONVERSION_MAPPING:
            v  = Decimal(q) * Decimal(BBL_CONVERSION_MAPPING[f])
            return v.quantize(Decimal('1.00'))


def get_production_by_month(m, y):
    """
    Takes two arguments: month, year
    returns total racking volume in bbl
    """
    MONTHS = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }

    monthly_racking = 0
    monthly_bottling = 0
    packages = Package.objects.filter(package_date__month=(MONTHS[m]), package_date__year=y)
    for p in packages:
        if 'CS' in p.format_type:
            monthly_bottling += to_bbl(p.format_type, p.format_qty)
        else:
            monthly_racking += to_bbl(p.format_type, p.format_qty)
    #return monthly_racking, monthly_bottling
    print(m, y, "Racking Volume:", monthly_racking)
    print(m, y, "Bottling Volume:", monthly_bottling)



def get_many_objects(queryset):
    """
    gets all objects from a queryset (manytomanyfields)
    returns comma-separated strings
    """
    return ", ".join([str(p) for p in queryset])


def one_year_from_now(y, m, d):
    one_year_out = datetime.date(y + 1, m, d)
    return one_year_out


# Class Models


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
        app_label = "packaging"



class Package(models.Model):
    NAME = (
        ("tyler", "Tyler"),
        ("ron", "Ron"),
        ("chris", "Chris"),
        ("shea", "Shea"),
        ("ian", "Ian"),
        ("brandon", "Brandon")
    )

    TYPE = (
        ('12oz/CS', '12oz/CS'),
        ('16oz/CS', '16oz/CS'),
        ('375ml/CS', '375ml/CS'),
        ('500ml/CS', '500ml/CS'),
        ('750ml/CS', '750ml/CS'),
        ('1/6bbl', '1/6bbl'),
        ('1/4bbl', '1/4bbl'),
        ('1/2bbl', '1/2bbl'),
        ('50l', '50l'),
        ('Firkin (10.8g)', 'Firkin (10.8g)'),
        ('Pin (5.4g)', 'Pin (5.4g)'),
    )

    package_date = models.DateField(default=timezone.now, blank=False, verbose_name="Date Packaged")
    packager = models.CharField("packager", max_length=100, choices=PACKAGER_NAME, blank=False)
    format_type = models.CharField("Format", max_length=20, choices=TYPE, blank=False)
    format_qty = models.DecimalField("Packaged Units", max_digits=10, decimal_places=2,
        help_text="Total packaged quantity for this format in cases/units (NOT BBL).", blank=False)
    batches = models.ManyToManyField('brewing.batch', help_text="Batches associated with this packaging event.",
        blank=False, verbose_name="Source Batches")
    oxygen_log = models.DecimalField("Packaging Oxygen Log", max_digits=5, decimal_places=2, blank=True, null=True, help_text="Enter measured oxygen (ppb).")

    def get_packaged_bbl(self):
        return to_bbl(self.format_type, self.format_qty)
    get_packaged_bbl.short_description = 'Packaged Vol(bbl)'


    def get_batches(self):
        if len(self.batches.all()) == 2:
            return str(self.batches.first().gyle) + ", " + str(self.batches.last().gyle)
        else:
            return str(self.batches.first().gyle)
    get_batches.short_description = 'Source Batch'


    def get_recipe(self):
        return str(self.batches.first().recipe)
    get_recipe.short_description = 'Source Recipe'


    def the_recipe(self):
        for batch in self.batches.all():
            return batch.recipe
    the_recipe.short_description = 'Source Recipe'


    def the_batches(self):
        for batch in self.batches.all():
            return batch.gyle
    the_batches.short_description = 'Source Batch'


    def __str__(self):
        return str(self.package_date) + ", " + str(self.the_recipe())


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.


    class Meta:
        ordering = ['-package_date']


class Aging(models.Model):
    
    NAME = (
        ("tyler", "Tyler"),
        ("ron", "Ron"),
        ("chris", "Chris"),
        ("shea", "Shea"),
        ("ian", "Ian"),
        ("brandon", "Brandon")
    )


    start_date = models.DateField(default=timezone.now, blank=True, verbose_name="Date Packaged")
    end_date = models.DateField(blank=True, verbose_name="Age Until This Date",
        default='')
    batches = models.ManyToManyField('brewing.batch', help_text="Batches sourced.",
        blank=True, null=True, verbose_name="Source Batches")
    barrel = models.ForeignKey('brewing.barrel', on_delete=models.CASCADE, blank=True, null=True)
    packager = models.CharField("packager", max_length=100, choices=NAME, blank=True, null=True)

    

    def get_batches(self):
        if len(self.batches.all()) == 2:
            return str(self.batches.first().gyle) + ", " + str(self.batches.last().gyle)
        else:
            return str(self.batches.first().gyle)
    get_batches.short_description = 'Source Batch'


    def the_recipe(self):
        for batch in self.batches.all():
            return batch.recipe
    the_recipe.short_description = 'Source Recipe'


    def __str__(self):
        return str(self.barrel)






