from django.contrib import admin
from .models import Package, Aging
# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
	list_display = ('package_date', 'packager', 'format_type', 'format_qty', 'get_packaged_bbl', 'get_batches', 'the_recipe')
	date_hierarchy = 'package_date'
	filter_horizontal = ('batches',)
@admin.register(Aging)
class AgeAdmin(admin.ModelAdmin):
	list_display = ('barrel', 'start_date', 'end_date', 'the_recipe', 'get_batches')