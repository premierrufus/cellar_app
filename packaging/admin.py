from django.contrib import admin
from .models import Package, Aging, to_bbl
# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
	list_display = ('package_date', 'packager', 'format_type', 'format_qty', 'get_packaged_bbl', 'get_batches', 'the_recipe')
	date_hierarchy = 'package_date'
	filter_horizontal = ('batches',)
	#search_fields = ['batches__recipe__name']
	list_filter = ('batches__recipe__name', 'package_date', 'format_type')
	actions = ['calc_total_production']


	def calc_total_production(self, request, queryset):
		query_bottling = 0
		query_racking = 0
		for obj in queryset:
			if 'CS' in obj.format_type:
				query_bottling += to_bbl(obj.format_type, obj.format_qty)
			else:
				query_racking += to_bbl(obj.format_type, obj.format_qty)
		self.message_user(request, "Total Bottled Volume: %s" % query_bottling)
		self.message_user(request, "Total Racked Volume: %s" % query_racking)
		#print("Total Bottled Volume:", query_bottling)
		#print("Total Racked Volume:", query_racking)
	calc_total_production.short_description = "Calculate production volume (bbl) for selected entries"

@admin.register(Aging)
class AgeAdmin(admin.ModelAdmin):
	list_display = ('barrel', 'start_date', 'end_date', 'the_recipe', 'get_batches')