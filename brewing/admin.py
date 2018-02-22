from django.contrib import admin
#from django.contrib.admin import AdminSite
from .models import Batch, Barrel, Gravity, Transfer, Container, Fermentable, Hop, Salt, Misc, Yeast, Recipe
# Register your models here.


admin.site.register(Barrel)
admin.site.register(Fermentable)
admin.site.register(Transfer)
admin.site.register(Gravity)
admin.site.register(Salt)
admin.site.register(Misc)
admin.site.register(Yeast)
admin.site.register(Recipe)

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
	list_display = ('gyle', 'recipe', 'brew_date', 'brewer', 'ferm_tank')
	fieldsets = (
        ('Batch Data', {
        	'classes': ('wide',),
            'fields': ('double_batch', 'gyle', 'recipe', 'ferm_tank', 'brewer', 'asst_brewer')
        }),
        ('Final Gravity/Attenuation/ABV', {
            'classes': ('collapse',),
            'fields': ('final_gravity', 'attenuation', 'final_abv')
        }),
        ('Plato', {
            'classes': ('collapse',),
            'fields': (('plato_1_val', 'plato_1_vol'), ('plato_2_val', 'plato_2_vol'), ('plato_3_val', 'plato_3_vol'))
        }),
        ('Transfer Data', {
            'classes': ('collapse',),
            'fields': ('pre_transfer_vol', 'post_transfer_vol', 'transfer_tank', 'transfer_log')
        }),
        ('Logs', {
            'classes': ('collapse',),
            'fields': ('cellaring_log', 'notes')
        })
    )


@admin.register(Hop)
class HopAdmin(admin.ModelAdmin):
	pass


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
	list_display = ('name', 'container_type', 'capacity')