from django.contrib import admin
from .models import Package
# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
	list_display = ('package_date', 'packager', 'format_type', 'format_qty', 'get_packaged_bbl', 'get_batches', 'the_recipe')


