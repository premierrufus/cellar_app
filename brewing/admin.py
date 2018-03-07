from django.contrib import admin
#from django.contrib.admin import AdminSite
from .models import Batch, Barrel, Container, Fermentable, Hop, Salt, Misc, Yeast, Recipe
# Register your models here.


admin.site.register(Barrel)
admin.site.register(Fermentable)
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
            'fields': (
                'double_batch',
                'brew_date',
                'gyle',
                'recipe', 
                'ferm_tank', 
                'brewer',
                'asst_brewer',
                'mash_temperature',
                'preboil_gravity',
                'preboil_volume',
                'postboil_gravity',
                'postboil_volume',
                'final_gravity', 
                'attenuation', 
                'final_abv', 
                'first_dry_hop',
                'second_dry_hop',
                'd_rest'
            )
        }),

        ('Gravity Log', {
            'classes': ('collapse',),
            'fields': (('gravity_1', 'gravity_1_date'), ('gravity_2', 'gravity_2_date'), ('gravity_3', 'gravity_3_date'))
        }),
        ('Transfer Data', {
            'classes': ('collapse',),
            'fields': ('pre_transfer_vol', 'post_transfer_vol', 'transfer_cip', 'transfer_date', 'transfer_tank', 'transfer_log')
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
	list_display = ('name', 'container_type', 'capacity', 'get_contents')