from django.contrib import admin
from .models import Package, Aging, to_bbl

import csv
from django.http import HttpResponse
# Register your models here.


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
	list_display = ('package_date', 'packager', 'format_type', 'format_qty', 'get_packaged_bbl', 'get_batches', 'the_recipe')
	date_hierarchy = 'package_date'
	filter_horizontal = ('batches',)
	#search_fields = ['batches__recipe__name']
	list_filter = ('batches__recipe__name', 'package_date', 'format_type')
	actions = ['calc_total_production', 'export_as_csv']


	def calc_total_production(self, request, queryset):
		"""
		Derives bbl production volume from selected entries on the django admin front-end
		uses imported to_bbl(format,quantity) function from packaging.models
		Flashes results to the admin screen with self.message_user
		"""
		query_bottling = 0
		query_racking = 0
		for obj in queryset:
			if 'CS' in obj.format_type:
				query_bottling += to_bbl(obj.format_type, obj.format_qty)
			else:
				query_racking += to_bbl(obj.format_type, obj.format_qty)
		self.message_user(request, "Total Bottled Volume: %s" % query_bottling)
		self.message_user(request, "Total Racked Volume: %s" % query_racking)
	calc_total_production.short_description = "Calculate production volume (bbl) for selected entries"


	def export_as_csv(self, request, queryset):
		"""
		exports selected rows to CSV
		"""
		meta = self.model._meta
		field_names = [field.name for field in meta.fields]

		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
		writer = csv.writer(response)

		writer.writerow(field_names)
		for obj in queryset:
			row = writer.writerow([getattr(obj,field) for field in field_names])

		return response
	export_as_csv.short_description = "Export selected packages (csv)"


@admin.register(Aging)
class AgeAdmin(admin.ModelAdmin):
	list_display = ('barrel', 'start_date', 'end_date', 'the_recipe', 'get_batches')