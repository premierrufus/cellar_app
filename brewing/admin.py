from django.contrib import admin
from .models import Batch, Barrel, Brix, Gravity, Transfer, Container, Fermentable, Hop, Salt, Misc, Yeast, Recipe
# Register your models here.


admin.site.register(Barrel)
admin.site.register(Fermentable)
admin.site.register(Transfer)
admin.site.register(Gravity)
admin.site.register(Brix)
admin.site.register(Salt)
admin.site.register(Misc)
admin.site.register(Yeast)
admin.site.register(Recipe)

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
	list_display = ('gyle', 'recipe', 'brew_date', 'brewer', 'current_tank' )


@admin.register(Hop)
class HopAdmin(admin.ModelAdmin):
	pass


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
	list_display = ('name', 'container_type', 'capacity')